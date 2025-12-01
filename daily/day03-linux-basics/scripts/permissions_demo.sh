#!/usr/bin/env bash

# Day 03: Permissions demonstration

echo "==> Creating secret.sh in playground/tmp..."
echo '#!/usr/bin/env bash' > playground/tmp/secret.sh
echo 'echo "Secret script running..."' >> playground/tmp/secret.sh

echo
echo "==> Initial permissions:"
ls -l playground/tmp/secret.sh

echo
echo "==> Adding execute permission for the user (u+x)..."
chmod u+x playground/tmp/secret.sh

echo
echo "==> Permissions after chmod:"
ls -l playground/tmp/secret.sh

echo
echo "==> Running secret.sh:"
./playground/tmp/secret.sh