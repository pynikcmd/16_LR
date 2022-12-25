#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from module_del_z import typer

if __name__ == '__main__':
    print(*typer("even")(2, 9, 4, 7, 8, 4, 2, 15))
