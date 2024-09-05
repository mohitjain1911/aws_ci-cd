#!/bin/bash
set -e

# Convert line endings
dos2unix /opt/codedeploy-agent/deployment-root/$eecd941b-7fd8-4280-a1a3-9d098c22f358/d-7BN7D7VV6/deployment-archive/scripts/start_container.sh
dos2unix /opt/codedeploy-agent/deployment-root/$eecd941b-7fd8-4280-a1a3-9d098c22f358/d-7BN7D7VV6/deployment-archive/scripts/stop_container.sh

# Execute the actual deployment scripts
/opt/codedeploy-agent/deployment-root/$eecd941b-7fd8-4280-a1a3-9d098c22f358/d-7BN7D7VV6/deployment-archive/scripts/start_container.sh
