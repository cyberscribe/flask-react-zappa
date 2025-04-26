#!/bin/bash
npm run clean
npm run build
aws s3 sync static s3://s3-example/ --exclude ".DS_Store" --cache-control max-age=60
source venv/bin/activate
cp .env.production .env
./venv/bin/zappa update production
aws cloudfront create-invalidation --distribution-id {ID_HERE --paths "/js/app.js" "/css/style.css" --output "text" --no-paginate
cp .env.dev .env
npm run clean