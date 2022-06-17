
INC=./include/
BIN=./bin/

SRCS=./sort_speed.c \
	./src/selection_sort.c 
	
EXE=sort_speed
CSV=speed_value.csv

all: $(EXE)
	
$(EXE): $(SRCS)  
	gcc -O3  -o $(BIN)$@ $^ -I$(INC) 

run:
	.\bin\$(EXE) 10000 10000 5 > ./result/$(CSV) 
	type .\result\$(CSV) 
	python plot_speed.py .\result\$(CSV)

