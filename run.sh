docker \
    -y \
    system \
    prune

docker-compose \
    -f docker-compose.win11.yml \
    down

docker-compose \
    -f docker-compose.win11.yml \
    up \
    --build