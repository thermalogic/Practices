
BIN=./bin/
INC=./include/

SRCS=./sort_speed.c \
	./src/selection_sort.c 

EXENAME=sort_speed
DATNAME=speed_value.csv

OUTFILE=$(BIN)$(EXENAME)

all: $(OUTFILE)
	
$(OUTFILE): $(SRCS)  
	gcc -O3  -o $@ $^ -I$(INC) 

run:
	.\bin\$(EXENAME) > ./result/$(DATNAME) 
	type .\result\$(DATNAME) 
	python plot_speed.py .\result\$(DATNAME)

