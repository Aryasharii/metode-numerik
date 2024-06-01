# Tugas Besar Metode Numerik

Ini adalah repositori untuk proyek tugas besar mata kuliah Metode Numerik di UPer.

### Table of contents

- [Projek Tugas Besar Metode Numerik](#tugas-besar-metode-numerik)
    - [Table of contents](#table-of-contents)
- [Main Project: Newton Cotes Implementation ](#main-project-newton-cotes-implementation-)
    - [Introduction ](#introduction-)
    - [Objective ](#objective-)
    - [Methodology ](#methodology-)
    - [Result ](#result-)
    - [Conclusion ](#conclusion-)

<br/>

# Main Project: Newton Cotes Implementation <a name="project"></a>

### Introduction <a name="prob"></a>

> **tldr**: _The constraint of requiring the number of subintervals to be divisible by three makes Simpson’s 3/8 rule less frequently used despite its accuracy for smooth functions._

```
Numerical methods are crucial in various fields for approximating definite integrals.
These methods are used to estimate curve areas, solve nonlinear equations, analyze milling process stability, and study the respiratory system.
Newton-Cotes methods, such as the midpoint rule, trapezoidal rule, Simpson’s 1/3 rule, and Simpson’s 3/8 rule, are popular for their accuracy in approximating
definite integrals by dividing the integration interval into smaller subintervals.
A study using the trapezoidal method with 36 partitions estimated West Java's area with a 3.51% error rate.
This study adopts Simpson’s 3/8 method to achieve a smaller error. Simpson’s 3/8 rule, while accurate for smooth functions,
requires the number of subintervals to be divisible by three, making it less common than other methods.
```

<br/>

### Objective <a name="sol"></a>

To compare the accuracy of calculating the area of West Java Province using the Trapezoidal rule and Simpson's 3/8 rule.

<br/>

### Methodology <a name="hw"></a>

The West Java province is divided into 4 regions. The area of each region was calculated using 9, 18, and 36 partitions with Python. The areas of all regions were then summed to approximate the total area. then the following formula was used:
##### Simpson's 3/8 Rule Formula:
![Method](https://github.com/Aryasharii/metode-numerik/blob/UAS/Method/Screenshot%202024-06-01%20164643.png)
<br/>
##### Relative Error Formula:
![Method](https://github.com/Aryasharii/metode-numerik/blob/UAS/Method/Screenshot%202024-06-01%20164929.png)

<br/>

### Result <a name="hwsetup"></a>

![Result](https://github.com/Aryasharii/metode-numerik/blob/UAS/Result/Screenshot%202024-06-01%20132947.png)

<br/>

### Conclusion <a name="comm"></a>

Calculation of the area of West Java province using Simpson's rule 3/8 has been proven to have better accuracy than the trapezoidal method, as evidenced by a smaller error value. 

<br/>
