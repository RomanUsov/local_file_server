How to run the server
=============================

It is necessary to run the server using Docker, this way we make sure the environment has all necessary libraries
in order to run correctly.
How to install Docker: https://docs.docker.com/desktop/


The following commands will show you how to build and run the local environment.

    $ docker-compose -f docker/docker-compose.yml build
    $ docker-compose -f docker/docker-compose.yml up


How to get inside the docker container
======================================

It is necessary to get inside the docker container of the local stack, since it has all required libraries. To do so,
make sure the local environment is up and running.

Open a terminal and run the following command::

    $ docker-compose -f docker/docker-compose.yml ps

You should see all the containers for the local server running.

Run the following command to get inside the "**file-server**" container::

    $ docker-compose -f docker/docker-compose.yml exec file-sever bash


How to share files
======================================

First of all, you nee the server up and running.
Check the IP address of your machine in the current network, e.g. `192.168.8.139`.
Put a file you would like to share in the `server/files` folder.
Then, you can use it as `http://192.168.8.139:8888/download/{file_name}`, where the `file_name` variable is the exact name of the file including its extension you would like to share in the local network.

Also it can be tested in any browser using this url.
