# Makefile for the simple page server.
#

# Nothing to install for this project.
install:
	@(echo 'nothing to install')

restart:
	@(make clean; make install; make start)

start:
	@(cd brevets; if [ -f ../dockerContainer.txt ]; then docker stop $$(cat ../dockerContainer.txt); fi; docker build -t project3 .; docker run -d $$(cat ../docker_ports.txt) project3 > ../dockerContainer.txt )

stop:
	@(cd brevets; docker stop $$(cat ../dockerContainer.txt))

terminal:
	@(cd brevets; docker exec -it $$(cat ../dockerContainer.txt) /bin/bash)

test:
	@(cd brevets; docker exec -it $$(cat ../dockerContainer.txt) ./run_tests.sh)

run:
	@(make restart)

logs:
	@(cd brevets; docker logs $$(cat ../dockerContainer.txt))

clean:
	@(cd brevets; docker stop $$(docker ps -a -q); docker rm $$(docker ps -a -q))


