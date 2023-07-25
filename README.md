# lims-demo

**LIMS Demo** is full-stack project, built and deployed over the course of **5 days**, where 
I aimed to demonstrate my development capabilities by quickly and efficiently building a 
minimum viable product for a Laboratory Information Management System (LIMS).

For more information, visit the documentation page at 
[lims-demo.readthedocs.io/](https://lims-demo.readthedocs.io/), or email me at 
[will@williampierce.io](mailto:will@williampierce.io)


# development

### Builds Docker images and spins up stack for development

```
docker-compose up
```

If you get an error relating to postgres or the psycopg2-binary package, it may be due to this project being developed on an Apple silicon machine. 

Possible resolutions include replacing psycopg2-binary with psycopg2, or specifying the build/target platform. 