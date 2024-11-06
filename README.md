## Points to Notice:

- First, we need to create a new network in docker: `docker network create metanet1`

- Then we need to add metanet in different services of existing project:

```
services:
    db_dev:
        networks:
            - metanet1

    redis:
        networks:
            - metanet1

    web:
        networks:
            - metanet1

    worker:
        networks:
            - metanet1

    beat:
        networks:
            - metanet1
```

- Now, configure the network in `docker-compose.yaml`:

```
networks:
  metanet1:
    external: true
```

- That's it!
