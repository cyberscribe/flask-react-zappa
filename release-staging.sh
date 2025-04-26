#!/bin/bash
npm run clean
npm run build-dev
aws s3 sync static s3://s3-example-staging/ --exclude ".DS_Store"  --size-only
source venv/bin/activate
cp .env.staging .env
./venv/bin/zappa update staging
aws cloudfront create-invalidation --distribution-id {ID_HERE} --paths "/js/app.js" "/css/style.css" --output "text" --no-paginate
cp .env.dev .env
npm run clean