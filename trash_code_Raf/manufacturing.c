#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    /*
A MANUFACTURING SYSTEM
k: The number of parallel washing stalls.
up: The state when a workstation is not broken down.
down: When a workstation is broken down and under repair.
dup: Die of a machine is not being changed.
ddown: Die of a machine is being changed.
b1, b2, b3: Number of sheets in in process buffers.
cb1, cb2, cb3: Cumulative values of b1, b2, b3.
maxb1, maxb2, maxb3: Capacities of in process buffers.
Sheet1: Number of sheets to be processed before a die change.
Stage: A workstation.
Counter: The counter of sheets output from the last stage.
kont: The number of observations of state of the systems.
clock: The record of elapsed time.
run: The time for which simulation is to be run (length of run).
rt: Repair time.
ttr1: Time to repair machine 1.
ut: time to failure.
ttf1: Time to failure of machine 1.
ttcd1:: Time to change die 1.
se1: Time to end processing of the current sheeton machine 1. */
    int k, up = 999, down = 777, dup = 888, ddown = 666;
    int b1 = 0, b2 = 0, b3 = 0, maxb1 = 1, maxb2 = 1, maxb3 = 1;
    long int cb1 = 0, cb2 = 0, cb3 = 0;
    int sheet1 = 500, sheet2 = 400, sheet3 = 750, sheet4 = 600;
    int stage1 = 22, stage2 = 22, stage3 - 22, stage4 = 22;
    int counter = 0, shear - up, punch - up, form - up, bend - up, shdie - dup, punchdie - dup, formdie - dup, bendie - dup;
    float r, kont, clock, run, delt, rt, ttrl, ttr2, ttr3, ttr;
    float ut = 0., ttf1, ttf2, ttf3, ttf4, ttcd1, ttcd2, ttcd3, ttcd4;
    floit sel - 4.0, e * 2 = 5 ., se3 - 5.0, se4 = 6.0;
    clock = 0.;
    delt = 1.0;
    kont = 0.;
    printf("\n Length of run=");
    scanf("%f", &run);
    r = rand() / 32768.;
    ttf1 = -100. ^ *log(1 - r);
    r = 1 rand() / 32768.;
    t f 2 = -90. ^ *log(1 - r);
    r = rand() / 32768.;
    ttf3 = -180. ^ *log(1 - r);
    r = rand() / 32768.;
    t f 4 = -240. ^ *log(1 - r);
    /*printf("\n %6.2f %6.2f $6.25 %6.2f", ttfl, ttf2, ttf3, ttf4); */