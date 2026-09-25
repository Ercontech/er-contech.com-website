#!/bin/bash
#
# Push Er-Con — sends both Er-Con repositories to GitHub.
#
#   Website   ~/Downloads/Claude - WebDev/ercon-site   -> RoloDev2026/Er-Con-website
#   Branding  ~/Downloads/Claude - Branding            -> RoloDev2026/Er-Con-Brand
#
#   (no flag)  double-click in Finder, or run in Terminal. Reports and waits.
#   --check    inspect without pushing anything.
#   --auto     unattended: commits anything uncommitted, pushes, never prompts.
#              This is what the daily scheduled job runs.
#
# This script never forces, never rewrites history and never deletes.
# The worst it can do is upload commits you already made.

set -uo pipefail

REPOS=(
  "Website:$HOME/Downloads/Claude - WebDev/ercon-site"
  "Branding:$HOME/Downloads/Claude - Branding"
)

MODE="${1:-}"
CHECK_ONLY=0; AUTO=0
[ "$MODE" = "--check" ] && CHECK_ONLY=1
[ "$MODE" = "--auto" ]  && AUTO=1

if [ $AUTO -eq 1 ]; then
  b=""; n=""; red=""; grn=""; yel=""
  echo "════ $(date '+%Y-%m-%d %H:%M') ════"
else
  b=$(tput bold 2>/dev/null); n=$(tput sgr0 2>/dev/null)
  red=$(tput setaf 1 2>/dev/null); grn=$(tput setaf 2 2>/dev/null); yel=$(tput setaf 3 2>/dev/null)
fi

problems=0
uncommitted=0

echo
echo "${b}Er-Con — push to GitHub${n}"
[ $CHECK_ONLY -eq 1 ] && echo "${yel}check only: nothing will be pushed${n}"
echo

for entry in "${REPOS[@]}"; do
  name="${entry%%:*}"
  dir="${entry#*:}"

  echo "${b}── $name ──${n}"

  if [ ! -d "$dir/.git" ]; then
    echo "  ${red}not a git repository:${n} $dir"
    echo "  Nothing pushed. Has the folder been moved or renamed?"
    problems=$((problems+1)); echo; continue
  fi

  cd "$dir" || { problems=$((problems+1)); continue; }

  # ---- uncommitted work -------------------------------------------------
  # A changed file that has not been committed is invisible to git push.
  # This is the one way to run this script, see success, and still not be
  # backed up. Interactively it is reported; unattended it is committed,
  # because an unread warning at 6:45pm protects nothing.
  changed=$(git status --porcelain --untracked-files=normal 2>/dev/null)
  if [ -n "$changed" ]; then
    count=$(printf '%s\n' "$changed" | wc -l | tr -d ' ')
    if [ $AUTO -eq 1 ]; then
      echo "  $count file(s) uncommitted — taking a snapshot"
      printf '%s\n' "$changed" | head -20 | sed 's/^/      /'
      git add -A
      git -c commit.gpgsign=false commit -q -m "Automatic daily snapshot — $(date '+%Y-%m-%d %H:%M')

Taken by the scheduled backup because these files were changed but never
committed. Not a considered commit: it is a safety net, and its only claim is
that this is what the folder looked like at this moment." \
        && echo "      snapshot committed" \
        || { echo "  ${red}snapshot failed${n}"; problems=$((problems+1)); }
    else
      echo "  ${yel}$count file(s) changed but not committed — these will NOT be pushed:${n}"
      printf '%s\n' "$changed" | head -12 | sed 's/^/      /'
      [ "$count" -gt 12 ] && echo "      … and $((count-12)) more"
      uncommitted=$((uncommitted+1))
      echo
    fi
  fi

  # ---- what is waiting to go -------------------------------------------
  branch=$(git rev-parse --abbrev-ref HEAD)
  git remote get-url origin >/dev/null 2>&1 || {
    echo "  ${red}no GitHub remote configured.${n} Nothing pushed."
    problems=$((problems+1)); echo; continue
  }

  waiting=0
  for br in $(git for-each-ref --format='%(refname:short)' refs/heads); do
    if git rev-parse --verify -q "origin/$br" >/dev/null 2>&1; then
      ahead=$(git rev-list --count "origin/$br..$br" 2>/dev/null || echo 0)
      [ "$ahead" -gt 0 ] && { echo "  $br: $ahead commit(s) to send"; waiting=$((waiting+ahead)); }
    else
      echo "  $br: new branch, not yet on GitHub"; waiting=$((waiting+1))
    fi
  done

  if [ "$waiting" -eq 0 ]; then
    echo "  ${grn}already up to date${n} — $branch at $(git rev-parse --short HEAD)"
    echo; continue
  fi

  if [ $CHECK_ONLY -eq 1 ]; then
    echo "  ${yel}(check only — not pushing)${n}"; echo; continue
  fi

  # ---- push -------------------------------------------------------------
  echo "  pushing…"
  if git push --all origin 2>&1 | sed 's/^/      /'; then
    echo "  ${grn}pushed${n} — $branch at $(git rev-parse --short HEAD)"
  else
    echo "  ${red}push failed.${n} Nothing on GitHub changed; your files are untouched."
    echo "  If it asked for a password, that is the access token, not your GitHub password."
    problems=$((problems+1))
  fi
  echo
done

# ---- summary -------------------------------------------------------------
echo "${b}──────────────${n}"
if [ "$problems" -gt 0 ]; then
  echo "${red}$problems repository/repositories had a problem — see above.${n}"
elif [ $CHECK_ONLY -eq 1 ]; then
  echo "${grn}Check complete.${n}"
else
  echo "${grn}Both repositories are on GitHub.${n}"
fi

if [ "$uncommitted" -gt 0 ]; then
  echo
  echo "${yel}Note:${n} $uncommitted folder(s) have edited files that were never committed."
  echo "Those changes exist only on this Mac. Ask Claude to commit them, or run:"
  echo "    git add -A && git commit -m \"what changed\""
  echo "then run this script again."
fi

echo
[ $AUTO -eq 1 ] && exit $([ "$problems" -gt 0 ] && echo 1 || echo 0)
read -r -p "Press return to close. "
