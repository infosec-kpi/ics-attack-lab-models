# ICS Attack Graph Models and SAT/SMT Analysis

This repository contains graph-based models of cyberattacks on Industrial Control Systems (ICS), as well as scripts and methodology for analyzing system vulnerabilities using SAT/SMT solvers (Z3).

The models and methods are based on the research article:

> **"Attack Models for Industrial Control System Elements Based on a Graph Approach and Countermeasures"**  
> Oleksii Novikov, Iryna Stopochkina, Andrii Voitsekhovskyi, Mykola Ilin  
> National Technical University of Ukraine "Igor Sikorsky KPI", 2025

---

## Features

- Logical attack graphs for several ICS attack scenarios represented with Boolean expressions in CNF for use with SMT/SAT solvers
- Python scripts using `z3-solver` for analysis 
- Case studies addressed: ARP spoofing, IFM controller attack, CaddyWiper malware
 

---

## Requirements

- Python 3.8+
- z3-solver (`pip install z3-solver`)

---

## 📁 Repository Structure

- optimize 
- solve 