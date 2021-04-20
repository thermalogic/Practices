
BIN=./bin/
INC=./include/

SRCS=./sortspeed.c \
	./src/utils.c  \
	./src/bubbleSort.c 

OUTFILE=$(BIN)sortspeed

all: $(OUTFILE)
	$(OUTFILE)

$(OUTFILE): $(SRCS)  
	gcc -O3 -o $@ $^ -I$(INC) 

run:
	$(OUTFILE)

