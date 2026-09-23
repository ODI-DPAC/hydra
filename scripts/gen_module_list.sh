#!/usr/bin/env bash
# Regenerate docs/software/bio-modules.md from the live module tree.
# Run on a Hydra login node, commit the result. Wire into a cron or a CI job that
# ssh-es to the cluster if you want it automatic.
#
#   ./scripts/gen_module_list.sh > docs/software/bio-modules.md
set -euo pipefail
PREFIX="${1:-bio}"   # module prefix to list; "bio" or "tools" etc.

cat << HDR
# Bioinformatics modules

Generated from \`module -t avail ${PREFIX}\` on $(date +%Y-%m-%d). Do not edit by hand; rerun \`scripts/gen_module_list.sh\`.

Load a package with \`module load ${PREFIX}/NAME/VERSION\`; \`(default)\` marks the version loaded when no version is given. The prefix \`bioinformatics/\` is an alias of \`${PREFIX}/\`. Every module on the cluster, including versions this list omits, is in the [list of module files](https://hydra.si.edu/tools/QSubGen/module-avail.html) and in \`module avail\` on a login node.

| Module | Versions |
|---|---|
HDR

# module -t avail prints one module per line; default versions are marked with (default) in some versions of module.
module -t avail "${PREFIX}" 2>&1 \
  | grep -E "^${PREFIX}/" \
  | sed -E "s#^${PREFIX}/##" \
  | awk -F/ "{ name=\$1; ver=(NF>1)?\$2:\"\"; v[name]=(name in v)?v[name] \", \" ver:ver } END { for (n in v) print \"| `\" n \"` | \" v[n] \" |\" }" \
  | sort
