
# Openiclib 
# OpenIClib

## Open Integrated Circuit Library 


**An open source library aggregating successfully taped-out, silicon proven open PDK designs that a) research groups, b) startups and c) integrated electronics & photonics students recur to for IC system-level design.**

## Organization & Contributing Guidelines

The library should be structured hierarchically: 1) PDK first, 2) Architecture category second, 3) Circuit block third;

- Each circuit block, independent of PDK, should contain core database file formats: SPICE, Verilog/A, for schematic, GDSII/OASIS for layout, LVS and DRC run result databases in JSON or text format); 
  
- Additional documentation, such as Markdown readme files, Jupyter Notebooks with Design Intent, should also be included (use IHP's tapeout data directory organization and content as standard);
  
- Any designs that have been successfully taped out and included into tapeout design databases can be initially symbolically linked to;
  
- Opportunity for having a silicon-proven blocks ported across multiple technologies;

- A gdsfactory-reviewed tapeout design meeting the required goals can be git-pushed and merged into the library - by any user.

## Objectives

Attracting people towards the usage of blocks within the  open IC design library would mean attracting users towards open PDKs - creating demand, decreasing tapeout costs and creating the pressure for reducing waiting time between tapeout runs. This constitutes an opportunity for gathering a user from academia and industry alike, once the main agents pushing for seamless integration, support and documentation of open PDKs are projects starting out (and remaining as) open source - including GDSFACTORY.