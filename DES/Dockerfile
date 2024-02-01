# Use an official lightweight Alpine image as a base image
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /app

# Install necessary tools for compiling C code and GDB for debugging
RUN apk --no-cache add build-base gdb

# Copy the source code into the container
COPY DESalgo.c .

# Compile the C code with debugging information
RUN gcc -g -o DESalgo DESalgo.c

# Specify the command to run GDB for debugging
CMD ["gdb", "./DESalgo"]
