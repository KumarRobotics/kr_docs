#!/usr/bin/env python
from __future__ import print_function
import sys
import matplotlib
import matplotlib.pyplot as plt
import yaml


def plot_airmax(tests, distances):
    plot_dict = {}
    for test in tests:
        mode = test['mode']
        antenna = test['antenna']
        test_data = test['data']
        if test['mode'] == 'airmax':
            for key in test_data:
                if key not in plot_dict:
                    fig, ax = plt.subplots()
                    plot_dict[key] = (fig, ax)
                    ax.set_title(mode + ' test')
                    ax.set_xlabel('distance [m]')
                    ax.set_ylabel(key)
                    ax.grid(True)
                ax = plot_dict[key][1]
                ax.plot(distances, test_data[key], marker='o', label=antenna)
                ax.legend()


def plot_bandwidth(tests, distances):
    key_to_plot = 'bandwidth'
    fig, ax = plt.subplots()
    ax.set_title('bandwidth comparison')
    ax.set_xlabel('distance [m]')
    ax.set_ylabel(key_to_plot + ' [Mbps]')
    for test in tests:
        mode = test['mode']
        antenna = test['antenna']
        test_data = test['data']
        print(test_data)
        for key in test_data:
            if key == key_to_plot:
                ax.plot(distances, test_data[key], marker='o', label=antenna)
    ax.grid(True)
    ax.legend()


def plot_data(tests, points, distances):
    plot_airmax(tests, distances)
    plot_bandwidth(tests, distances)
    plt.show()


def main():
    # Load yaml file
    fs = open("/home/chao/Desktop/data.yaml", 'r')
    for data in yaml.load_all(fs):
        if 'date' in data:
            date = data['date']
            distances = data['distance']
            points = data['points']
        else:
            tests = data

    matplotlib.rcParams.update({'font.size': 14})
    plot_data(tests, points, distances)


if __name__ == '__main__':
    sys.exit(main())