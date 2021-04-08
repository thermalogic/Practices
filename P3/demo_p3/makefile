
BIN=./bin/
INC=./include/

SRCS=./sortspeed.c \
	./src/utils.c  \
	./src/bubbleSort.c 

OUTFILE=./bin/sortspeed

all: $(OUTFILE)
	$(OUTFILE)

$(OUTFILE): $(SRCS)  
	gcc -O3 -o $@ $^ -I$(INC) 

run:
	$(OUTFILE)

