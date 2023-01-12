<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
# Egeria CTS Test Repository

This repository provides a daily or ad-hoc scheduled action to run Egeria's conformance test suite again
 - Inmemory repository
 - Local Graph Repository
 - XTDB 

Review the 'actions' tag for latest executions and results. There you should find
 - a tabular view of profile results, including indicating number of tests passed and failed
 - attachments with a detailed archive containing all the output from the test such as failed assertions

## Known issues / limitations

- only test one version of code (main/latest)
- no support for PRs
- Execution time may exceed 6h in which case test will fail
- Some CTS tests are timing sensitive and can fail in some environments
- XTDB version is encoded in the download string in etc/xtdb.yaml
