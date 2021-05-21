
BIN=./bin/
INC=./include/

SRCS=./sortspeed.c \
	./src/utils.c  \
	./src/bubble_sort.c 

OUTFILE=$(BIN)sortspeed

all: $(OUTFILE)
	$(OUTFILE)

$(OUTFILE): $(SRCS)  
	gcc -O3 -o $@ $^ -I$(INC) 

run:
	$(OUTFILE)

