#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:

    def __init__(self, data):
        self.set_data(data)

    def set_data(self, data):
        self.data = sorted(data)
        self.length = len(self.data)
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.stand_dev = self._calc_std()

    def add_data(self, new_data):
        self.data.extend(new_data)
        self.set_data(self.data)

    def remove_data(self, bad_data):
        self.data = [elem for elem in self.data if elem not in bad_data]
        self.set_data(self.data)

    def _calc_mean(self):
        return sum(self.data)/len(self.data)

    def _calc_median(self):
        middle_point = int(self.length/2)
        if self.length%2:
            return self.data[middle_point]
        else:
            return (self.data[middle_point] + self.data[middle_point - 1 ])/2

    def _calc_variance(self):
        return sum([(datum -  self.mean)**2 for datum in self.data])/(self.length - 1)

    def _calc_std(self):
        return self._calc_variance()**0.5
