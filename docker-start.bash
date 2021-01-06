#!/bin/bash

# sudo docker run -it -p 3000:5000 --name management-tool -e ARROWHEAD_SR_URL=htpps://localhost:8342 -e ARROWHEAD_ORCH_URL=htpps://localhost:8340 -e ARROWHEAD_GK_URL=htpps://localhost:8348 svetlint/management-tool

sudo docker run -it -p 3000:5000 --name management-tool -e REACT_APP_ARROWHEAD_SR_URL=https://localhost:8443 -e REACT_APP_ARROWHEAD_AUTH_URL=https://localhost:8445 -e REACT_APP_ARROWHEAD_ORCH_URL=https://localhost:8441 -e REACT_APP_ARROWHEAD_GK_URL=https://localhost:8449 -e REACT_APP_ARROWHEAD_GW_URL=https://localhost:8453 -e REACT_APP_ARROWHEAD_EH_URL=https://localhost:8455 svetlint/management-tool
