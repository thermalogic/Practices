#
# python plot_speed.py datefilename
#
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def plot_speedvalue(filename):
    csvfile = open(filename, encoding='UTF-8')
    csvdata = csv.DictReader(csvfile)
    table ={item:[] for item in csvdata.fieldnames}
    for line in csvdata:
        for key in line.keys():
            table[key].append(int(line[key]))
    csvfile.close()  

    fig = plt.figure(figsize=(6, 6))
    plt.title('Sort Speed(microseconds)')
    plt.xlabel('A Size')
    plt.ylabel('microseconds')

    plt.xlim(table["A_size"][0], table["A_size"][-1])
    x = np.array(table["A_size"])
    for item in list(table.keys())[1:]:
        y = np.array(table[item])
        # data points with log scale
        plt.loglog(x,y, "*", label=item)
        # smooth curve with interpolating B-spline
        spl = make_interp_spline(x, y,k=2)
        x_smooth = np.linspace(x.min(), x.max(), 2000)
        y_smooth = spl(x_smooth)
        plt.loglog(x_smooth, y_smooth)

    plt.legend(loc="best")
    plt.show()

if __name__ == "__main__":
    import sys
    plot_speedvalue(sys.argv[1])
