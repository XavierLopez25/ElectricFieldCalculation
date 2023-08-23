# Electric Field Calculator

![Electric Field Banner](https://i.ytimg.com/vi/H6lb46AiXHQ/maxresdefault.jpg)

This application is designed to visualize and calculate the electric fields generated by different charge distributions, such as rings, disks, and line charges. Developed by **Madeline Castro** and **Xavier López**, enthusiastic physics students from Universidad del Valle de Guatemala.

## Overview

The program provides an interface where users can choose the type of charge distribution, set parameters, and calculate the resultant electric field at a specific point. The results are visualized graphically, helping in understanding the nature of electric fields produced by various charge distributions.

## On Precision and Exactness

In the realm of computational physics, it's essential to understand the difference between exactness and precision. Due to inherent limitations in numerical methods and floating-point arithmetic, some calculations might not yield "exact" results. However, this does not necessarily mean they aren't precise.

For instance, the application uses the `quad` function from the `scipy.integrate` module to perform numerical integration. The parameters `epsabs` and `epsrel` are set to `1.49e-12`, meaning the absolute and relative errors in the integration are bound within this threshold. This ensures a high degree of precision, even if the results can't be exact due to the approximations intrinsic to numerical methods.

## Features

- Intuitive interface to input charge distributions and parameters.
- Visual representation of the charge distribution and resultant electric field.
- Precision-bound calculations to ensure reliable results.
- Developed using libraries such as `tkinter` for GUI, `numpy` for numerical operations, and `matplotlib` for visualization.

## Authors (4th Semester CS & TI Students at Universidad del Valle de Guatemala)

- **Madeline Castro**
- **Xavier López**

## Acknowledgments

We'd like to extend our gratitude to the professors and colleagues at Universidad del Valle de Guatemala for their invaluable insights and feedback.
