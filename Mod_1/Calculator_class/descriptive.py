#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:

    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.mean = self._calc_mean(data)
        self.median = self._calc_median(data)
        self.variance = self._calc_variance(data)
        self.stand_dev = self._calc_std(data)

    def add_data(self, new_data):
        self.data = self.data.extend(new_data)
        self.__init__(self, self.data)

    def remove_data(self, bad_data):
        self.data = [elem for elem in self.data if elem not in bad_data]
        self.__init__(self, self.data)

    def _calc_mean(self, data):
        return sum(data)/len(data)

    def _calc_median(self, data):
        sorted_data = data.sort()
        middle_point = int(len(data)/2)
        if len(data)%2:
            return data[middle_point]
        else:
            return (data[middle_point] + data[middle_point - 1 ])/2

    def _calc_variance(self, data):
        return sum([(datum -  self._calc_mean(data))**2 for datum in data])/(len(data) - 1)

    def _calc_std(self, data):
        return self._calc_variance(data)**0.5
