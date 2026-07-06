---
title: Library
---

# Design Library

<div class="catalog-controls">
  <input type="text" id="filter-search" placeholder="Search designs..." class="catalog-search">
  <div class="catalog-filters">
    <select id="filter-pdk" class="catalog-select">
    <option value="all">All PDKs</option>
    <option value="gf180">Gf180</option>
    <option value="ihp130sg">Ihp130Sg</option>
    <option value="skywater130">Skywater130</option>
    <option value="unknown">Unknown</option>
    </select>
    <select id="filter-class" class="catalog-select">
    <option value="all">All Classes</option>
    <option value="analog">Analog</option>
    <option value="digital">Digital</option>
    <option value="mixed-signal">Mixed Signal</option>
    <option value="optical">Optical</option>
    <option value="unknown">Unknown</option>
    </select>
    <select id="filter-type" class="catalog-select">
    <option value="all">All Types</option>
    <option value="ADC">Adc</option>
    <option value="Bandgap">Bandgap</option>
    <option value="DAC">Dac</option>
    <option value="Filter">Filter</option>
    <option value="Frequency Divider">Frequency Divider</option>
    <option value="GPIO">Gpio</option>
    <option value="LDO">Ldo</option>
    <option value="LNA">Lna</option>
    <option value="OTA">Ota</option>
    <option value="Op-Amp">Op Amp</option>
    <option value="Oscillator">Oscillator</option>
    <option value="Power Amplifier">Power Amplifier</option>
    <option value="Processor">Processor</option>
    <option value="RISC-V Core">Risc V Core</option>
    <option value="Reference">Reference</option>
    <option value="Regulator">Regulator</option>
    <option value="SERDES">Serdes</option>
    <option value="SRAM">Sram</option>
    <option value="SoC">Soc</option>
    <option value="TIA">Tia</option>
    <option value="VCO">Vco</option>
    <option value="unknown">Unknown</option>
    </select>
    <label class="catalog-toggle">
      <input type="checkbox" id="filter-proven">
      Silicon proven only
    </label>
  </div>
</div>

<p id="catalog-count" class="catalog-count"></p>

<div class="catalog-grid" id="catalog-grid">
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="analog"
     data-types="LNA"
     data-proven="true"
     data-name="160 ghz low noise amplifier with 27-ghz bandwidth">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Apr2025/tree/main/160GHz_LNA" target="_blank" rel="noopener">160 GHz Low Noise Amplifier with 27-GHz Bandwidth</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">A Low Noise Amplifier (LNA) designed in IHP SG13G2 BiCMOS technology achieving 5.77 dB noise figure at 160 GHz with 27 GHz bandwidth (146-173 GHz) and 12.5 dB peak gain.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">LNA</span>
  </div>
  <div class="card-specs"><span class="card-spec">bandwidth: 146-173 GHz</span><span class="card-spec">noise figure: 5.77 dB @ 160 GHz</span><span class="card-spec">peak gain: 12.5 dB @ 157 GHz</span><span class="card-spec">input p1db: -11.4 dBm @ 160 GHz</span></div>
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Apr2025/tree/main/160GHz_LNA" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/TO_Apr2025</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="analog"
     data-types="TIA"
     data-proven="true"
     data-name="low-noise single ended tia with 40-ghz bandwidth">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Apr2025/tree/main/40_GHZ_LOW_NOISE_TIA" target="_blank" rel="noopener">Low-Noise Single Ended TIA with 40-GHz Bandwidth</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">A DC to 40 GHz Single Ended Transimpedance Amplifier (TIA) in IHP SG13G2 BiCMOS technology optimized for low input-referred current noise density of ~9.5 pA/√Hz.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">TIA</span>
  </div>
  <div class="card-specs"><span class="card-spec">bandwidth: DC to 40 GHz</span><span class="card-spec">input noise density: ~9.5 pA/√Hz</span><span class="card-spec">topology: single-ended</span></div>
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Apr2025/tree/main/40_GHZ_LOW_NOISE_TIA" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/TO_Apr2025</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="caravel">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/caravel" target="_blank" rel="noopener">Caravel</a></h3>
    
  </div>
  <p class="card-summary">Caravel is a standard SoC template with on chip resources to control and read/write operations from a user-dedicated space.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/caravel" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/caravel</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="true"
     data-name="caravel mpw one">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/caravel_mpw-one" target="_blank" rel="noopener">Caravel Mpw One</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">Caravel is a standard SoC hardness with on chip resources to control and read/write operations from a user-dedicated space.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/caravel_mpw-one" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/caravel_mpw-one</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="sram sky130">
  <div class="card-header">
    <h3><a href="https://github.com/ShonTaware/SRAM_SKY130" target="_blank" rel="noopener">Sram Sky130</a></h3>
    
  </div>
  <p class="card-summary">Design of 1024x32 SRAM (32Kbits) using OpenRAM and SKY130 PDKs with operating voltage of 1.8V and access time &lt; 2.5ns</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ShonTaware/SRAM_SKY130" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ShonTaware/SRAM_SKY130</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="acm mosfet models">
  <div class="card-header">
    <h3><a href="https://github.com/ACMmodel/ACM-MOSFET-models" target="_blank" rel="noopener">Acm Mosfet Models</a></h3>
    
  </div>
  <p class="card-summary">A simple MOSFET model with only 5-DC-parameters for circuit simulation</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ACMmodel/ACM-MOSFET-models" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ACMmodel/ACM-MOSFET-models</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="LDO"
     data-proven="false"
     data-name="sky130 ldo rl">
  <div class="card-header">
    <h3><a href="https://github.com/ChrisZonghaoLi/sky130_ldo_rl" target="_blank" rel="noopener">Sky130 Ldo Rl</a></h3>
    
  </div>
  <p class="card-summary">This repo contains the code that runs RL+GNN to optimize LDOs in SKY130 process.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">LDO</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ChrisZonghaoLi/sky130_ldo_rl" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ChrisZonghaoLi/sky130_ldo_rl</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="ADC"
     data-proven="false"
     data-name="sky130 sar adc">
  <div class="card-header">
    <h3><a href="https://github.com/w32agobot/SKY130_SAR-ADC" target="_blank" rel="noopener">Sky130 Sar Adc</a></h3>
    
  </div>
  <p class="card-summary">Fully-differential asynchronous non-binary 12-bit SAR-ADC</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">ADC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/w32agobot/SKY130_SAR-ADC" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> w32agobot/SKY130_SAR-ADC</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="ralf">
  <div class="card-header">
    <h3><a href="https://github.com/JakobRat/RALF" target="_blank" rel="noopener">Ralf</a></h3>
    
  </div>
  <p class="card-summary">Reinforcement learning assisted analog layout design flow.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/JakobRat/RALF" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> JakobRat/RALF</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="skywater pdk libs sky130 fd bd sram">
  <div class="card-header">
    <h3><a href="https://github.com/google/skywater-pdk-libs-sky130_fd_bd_sram" target="_blank" rel="noopener">Skywater Pdk Libs Sky130 Fd Bd Sram</a></h3>
    
  </div>
  <p class="card-summary">SRAM build space for SKY130 provided by SkyWater.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/google/skywater-pdk-libs-sky130_fd_bd_sram" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> google/skywater-pdk-libs-sky130_fd_bd_sram</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="unknown"
     data-proven="true"
     data-name="blake2 asic">
  <div class="card-header">
    <h3><a href="https://github.com/Essenceia/blake2_asic" target="_blank" rel="noopener">Blake2 Asic</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">SKY130A implementatoin of the Blake2s hash algorithm</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Essenceia/blake2_asic" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Essenceia/blake2_asic</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="unknown"
     data-proven="false"
     data-name="sky130rhbdlib">
  <div class="card-header">
    <h3><a href="https://github.com/stineje/sky130RHBDlib" target="_blank" rel="noopener">Sky130Rhbdlib</a></h3>
    
  </div>
  <p class="card-summary">Open-source RHBD (Radiation Hardened by Design)  Standard-Cell Library for SKY130</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/stineje/sky130RHBDlib" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> stineje/sky130RHBDlib</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="unknown"
     data-proven="false"
     data-name="ms qspi xip cache">
  <div class="card-header">
    <h3><a href="https://github.com/shalan/MS_QSPI_XIP_CACHE" target="_blank" rel="noopener">Ms Qspi Xip Cache</a></h3>
    
  </div>
  <p class="card-summary">AHB-Lite Quad I/O SPI Flash memory controller with direct mapped cache and support for XiP</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/shalan/MS_QSPI_XIP_CACHE" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> shalan/MS_QSPI_XIP_CACHE</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="LDO Regulator"
     data-proven="false"
     data-name="low dropout voltage regulator ldo using sky130pdk">
  <div class="card-header">
    <h3><a href="https://github.com/chennakeshavadasa/Low-dropout-Voltage-Regulator-LDO-using-SKY130PDK" target="_blank" rel="noopener">Low Dropout Voltage Regulator Ldo Using Sky130Pdk</a></h3>
    
  </div>
  <p class="card-summary">Design of LDO using open source SKY130PDK</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">LDO, Regulator</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chennakeshavadasa/Low-dropout-Voltage-Regulator-LDO-using-SKY130PDK" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chennakeshavadasa/Low-dropout-Voltage-Regulator-LDO-using-SKY130PDK</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="OTA Op-Amp"
     data-proven="false"
     data-name="miller compensated two stage opamp using sky130pdk">
  <div class="card-header">
    <h3><a href="https://github.com/chennakeshavadasa/Miller-Compensated-Two-stage-OPAMP-using-SKY130PDK" target="_blank" rel="noopener">Miller Compensated Two Stage Opamp Using Sky130Pdk</a></h3>
    
  </div>
  <p class="card-summary">Design of miller compensated 2 stage opamp using open source SKY130PDK</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">OTA, Op-Amp</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chennakeshavadasa/Miller-Compensated-Two-stage-OPAMP-using-SKY130PDK" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chennakeshavadasa/Miller-Compensated-Two-stage-OPAMP-using-SKY130PDK</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="ADC"
     data-proven="false"
     data-name="sky130 ct dsm">
  <div class="card-header">
    <h3><a href="https://github.com/michaelk99/SKY130_CT-DSM" target="_blank" rel="noopener">Sky130 Ct Dsm</a></h3>
    
  </div>
  <p class="card-summary">A case study of a continuous-time Delta-Sigma modulator including system-level simulations/design of the CT-DSM, circuit-design of the front-end Gm-cell and a mixed-signal simulation w/ Ngspice.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">ADC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/michaelk99/SKY130_CT-DSM" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> michaelk99/SKY130_CT-DSM</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="pmicgen">
  <div class="card-header">
    <h3><a href="https://github.com/pmicgen/pmicgen" target="_blank" rel="noopener">Pmicgen</a></h3>
    
  </div>
  <p class="card-summary">Automated generation of a PMIC</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/pmicgen/pmicgen" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> pmicgen/pmicgen</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="unknown"
     data-proven="false"
     data-name="esim hackathon">
  <div class="card-header">
    <h3><a href="https://github.com/PSR0001/eSim_hackathon" target="_blank" rel="noopener">Esim Hackathon</a></h3>
    
  </div>
  <p class="card-summary">Mixed Signal Circuit Design and Simulation Marathon under very Good category  Article: https://www.linkedin.com/pulse/mixed-signal-simulation-marathon-using-esim-sky130-kannan-moudgalya/?trackingId=PLrgw35VThqQ5QB</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/PSR0001/eSim_hackathon" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> PSR0001/eSim_hackathon</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="OTA Op-Amp"
     data-proven="false"
     data-name="2ac folded cascode ota with sky130 pdk">
  <div class="card-header">
    <h3><a href="https://github.com/ridvanumaz/2AC_Folded-Cascode-OTA-with-SKY130-PDK" target="_blank" rel="noopener">2Ac Folded Cascode Ota With Sky130 Pdk</a></h3>
    
  </div>
  <p class="card-summary">A folded-cascode OTA with 3.3V power supply and 54.27 dB DC gain with 66.8MHz unity frequency</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">OTA, Op-Amp</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ridvanumaz/2AC_Folded-Cascode-OTA-with-SKY130-PDK" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ridvanumaz/2AC_Folded-Cascode-OTA-with-SKY130-PDK</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="DAC"
     data-proven="true"
     data-name="tt08 vga fun">
  <div class="card-header">
    <h3><a href="https://github.com/algofoogle/tt08-vga-fun" target="_blank" rel="noopener">Tt08 Vga Fun</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">Attempt at 24-bit (RGB888) VGA DAC</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">DAC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/algofoogle/tt08-vga-fun" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> algofoogle/tt08-vga-fun</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="unknown"
     data-proven="true"
     data-name="tt07 raybox zero">
  <div class="card-header">
    <h3><a href="https://github.com/algofoogle/tt07-raybox-zero" target="_blank" rel="noopener">Tt07 Raybox Zero</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">TT07 resub of tt04-raybox-zero &quot;3D&quot; VGA ray caster demo (like Wolf3D)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/algofoogle/tt07-raybox-zero" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> algofoogle/tt07-raybox-zero</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Filter"
     data-proven="false"
     data-name="fir filter gds2 flow">
  <div class="card-header">
    <h3><a href="https://github.com/paramsaini87/fir-filter-gds2-flow" target="_blank" rel="noopener">Fir Filter Gds2 Flow</a></h3>
    
  </div>
  <p class="card-summary">Complete RTL-to-GDSII flow for 32-tap FIR filter on SKY130 130nm — 33% fewer cells than OpenLane, formally verified (SAT proof), DRC/LVS clean</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Filter</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/paramsaini87/fir-filter-gds2-flow" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> paramsaini87/fir-filter-gds2-flow</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="Bandgap"
     data-proven="false"
     data-name="rply bias sky130nm">
  <div class="card-header">
    <h3><a href="https://github.com/wulffern/rply_bias_sky130nm" target="_blank" rel="noopener">Rply Bias Sky130Nm</a></h3>
    
  </div>
  <p class="card-summary">PTAT bias current source for sky130nm</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">Bandgap</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/wulffern/rply_bias_sky130nm" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> wulffern/rply_bias_sky130nm</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="nasscom vsd soc">
  <div class="card-header">
    <h3><a href="https://github.com/Tanmay707/NASSCOM-VSD-SOC" target="_blank" rel="noopener">Nasscom Vsd Soc</a></h3>
    
  </div>
  <p class="card-summary">This Repository consists of the learnings and simulations using OpenLANE under the workshop by VSD entitled as SOC Design and Planning Workshop</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Tanmay707/NASSCOM-VSD-SOC" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Tanmay707/NASSCOM-VSD-SOC</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="ADC"
     data-proven="false"
     data-name="tiny sar">
  <div class="card-header">
    <h3><a href="https://github.com/Revenantx86/tiny-SAR" target="_blank" rel="noopener">Tiny Sar</a></h3>
    
  </div>
  <p class="card-summary">8-bit Succesive approximation register analog to digital converter (SAR-ADC)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">ADC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Revenantx86/tiny-SAR" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Revenantx86/tiny-SAR</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="unknown"
     data-proven="false"
     data-name="cs amp sky130">
  <div class="card-header">
    <h3><a href="https://github.com/junior-jl/cs-amp-sky130" target="_blank" rel="noopener">Cs Amp Sky130</a></h3>
    
  </div>
  <p class="card-summary">Design of a common source amplifier using Skywater sky130 technology</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/junior-jl/cs-amp-sky130" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> junior-jl/cs-amp-sky130</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="digital vlsi soc design and planning">
  <div class="card-header">
    <h3><a href="https://github.com/ShyamRazesh/DIGITAL-VLSI-SOC-DESIGN-AND-PLANNING" target="_blank" rel="noopener">Digital Vlsi Soc Design And Planning</a></h3>
    
  </div>
  <p class="card-summary">2 Week digital VLSI SoC design and planning workshop with complete RTL2GDSII flow organized by VSD in collaboration with NASSCOM (Advanced Physical Design using OpenLANE /Sky130)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ShyamRazesh/DIGITAL-VLSI-SOC-DESIGN-AND-PLANNING" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ShyamRazesh/DIGITAL-VLSI-SOC-DESIGN-AND-PLANNING</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="unknown"
     data-proven="false"
     data-name="cmos circuit design and simulation using sky130">
  <div class="card-header">
    <h3><a href="https://github.com/saivarshithm/CMOS-Circuit-Design-and-Simulation-Using-SKY130" target="_blank" rel="noopener">Cmos Circuit Design And Simulation Using Sky130</a></h3>
    
  </div>
  <p class="card-summary">CMOS circuit design and SPICE simulation study covering NMOS behavior, inverter VTC, noise margins, and robustness analysis.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/saivarshithm/CMOS-Circuit-Design-and-Simulation-Using-SKY130" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> saivarshithm/CMOS-Circuit-Design-and-Simulation-Using-SKY130</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="Oscillator"
     data-proven="true"
     data-name="ttsky tetrahedral oscillator">
  <div class="card-header">
    <h3><a href="https://github.com/ROMERUU-dev/ttsky-tetrahedral-oscillator" target="_blank" rel="noopener">Ttsky Tetrahedral Oscillator</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">This project implements a tetrahedral oscillator inspired by the paper “Analysis and Design of a Tetrahedral Oscillator” by Richelle L. Smith and Thomas H. Lee. The oscillator is built from coupled inverter pairs, and its operating frequency is tuned by adding capacitive loads to the internal nodes.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">Oscillator</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ROMERUU-dev/ttsky-tetrahedral-oscillator" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ROMERUU-dev/ttsky-tetrahedral-oscillator</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="unknown"
     data-proven="false"
     data-name="open vlsi">
  <div class="card-header">
    <h3><a href="https://github.com/puxina/Open-VLSI" target="_blank" rel="noopener">Open Vlsi</a></h3>
    
  </div>
  <p class="card-summary">Repository for open-source tools to VLSI design</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/puxina/Open-VLSI" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> puxina/Open-VLSI</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="neoram">
  <div class="card-header">
    <h3><a href="https://github.com/muditbhargava66/NeoRAM" target="_blank" rel="noopener">Neoram</a></h3>
    
  </div>
  <p class="card-summary">Advanced SRAM Controller with ECC Support for Sky130 Process - Production-Ready Multi-Port Memory System.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/muditbhargava66/NeoRAM" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> muditbhargava66/NeoRAM</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="DAC Filter SoC"
     data-proven="false"
     data-name="fir accel caravel soc">
  <div class="card-header">
    <h3><a href="https://github.com/Mummanajagadeesh/fir-accel-caravel-soc" target="_blank" rel="noopener">Fir Accel Caravel Soc</a></h3>
    
  </div>
  <p class="card-summary">Mixed-signal FIR accelerator SoC on Caravel/Sky130A — CIC decimator, 8-tap programmable FIR filter, PWM DAC, Wishbone CSR</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">DAC, Filter, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Mummanajagadeesh/fir-accel-caravel-soc" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Mummanajagadeesh/fir-accel-caravel-soc</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="openlane2 sram">
  <div class="card-header">
    <h3><a href="https://github.com/Samizo-AITL/openlane2-sram" target="_blank" rel="noopener">Openlane2 Sram</a></h3>
    
  </div>
  <p class="card-summary">OpenLane2 example project for integrating an SRAM hard macro and generating GDS.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Samizo-AITL/openlane2-sram" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Samizo-AITL/openlane2-sram</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="ieee summer school on semiconductor devices integrated circuits 2025">
  <div class="card-header">
    <h3><a href="https://github.com/Additrejo/IEEE-Summer-School-on-Semiconductor-Devices-Integrated-Circuits-2025" target="_blank" rel="noopener">Ieee Summer School On Semiconductor Devices Integrated Circuits 2025</a></h3>
    
  </div>
  <p class="card-summary">IEEE Summer School on Semiconductor Devices &amp; Integrated Circuits 2025 por Nanociencias y Micro y Nanotecnologías del Instituto Politécnico Nacional</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Additrejo/IEEE-Summer-School-on-Semiconductor-Devices-Integrated-Circuits-2025" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Additrejo/IEEE-Summer-School-on-Semiconductor-Devices-Integrated-Circuits-2025</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="risc v multiprecision processor core">
  <div class="card-header">
    <h3><a href="https://github.com/ridash2005/RISC-V_MultiPrecision_Processor_Core" target="_blank" rel="noopener">Risc V Multiprecision Processor Core</a></h3>
    
  </div>
  <p class="card-summary">A synthesizable RISC-V processor ecosystem in SystemVerilog. Features 32/64-bit single-cycle and 5-stage pipelined architectures, ASIC-proven on Sky130.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ridash2005/RISC-V_MultiPrecision_Processor_Core" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ridash2005/RISC-V_MultiPrecision_Processor_Core</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="upb natalius soc">
  <div class="card-header">
    <h3><a href="https://github.com/fguzman82/upb_natalius_soc" target="_blank" rel="noopener">Upb Natalius Soc</a></h3>
    
  </div>
  <p class="card-summary">8 bit RISC Processor for SKY 130nm process</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/fguzman82/upb_natalius_soc" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> fguzman82/upb_natalius_soc</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="nocrouter rtl2gdsii">
  <div class="card-header">
    <h3><a href="https://github.com/VLSI-Shubh/NoCRouter-RTL2GDSII" target="_blank" rel="noopener">Nocrouter Rtl2Gdsii</a></h3>
    
  </div>
  <p class="card-summary">A complete 1×3 NoC router implemented from RTL to GDSII using the Sky130A PDK. Includes full functional verification, synthesis (Yosys), and physical design using OpenLane/OpenROAD, culminating in a signoff-clean GDS layout.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/VLSI-Shubh/NoCRouter-RTL2GDSII" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> VLSI-Shubh/NoCRouter-RTL2GDSII</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="open source asic design rtl to gdsii">
  <div class="card-header">
    <h3><a href="https://github.com/hemachandhran/Open-Source-ASIC-Design-RTL-to-GDSII" target="_blank" rel="noopener">Open Source Asic Design Rtl To Gdsii</a></h3>
    
  </div>
  <p class="card-summary">Hands-on open-source ASIC design portfolio documenting the complete RTL-to-GDSII flow, SoC verification, and gate-level simulation using OpenLane, OpenROAD, SKY130, Caravel, and VSDSquadron.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/hemachandhran/Open-Source-ASIC-Design-RTL-to-GDSII" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> hemachandhran/Open-Source-ASIC-Design-RTL-to-GDSII</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Reference RISC-V Core SoC"
     data-proven="true"
     data-name="risc v reference soc tapeout program phase 2">
  <div class="card-header">
    <h3><a href="https://github.com/ShekharShwetank/RISC-V_Reference_SoC_Tapeout_Program_Phase_2" target="_blank" rel="noopener">Risc V Reference Soc Tapeout Program Phase 2</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">RISC-V Reference SoC Design and Tapeout Program Phase 2 personal documentation</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Reference, RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ShekharShwetank/RISC-V_Reference_SoC_Tapeout_Program_Phase_2" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ShekharShwetank/RISC-V_Reference_SoC_Tapeout_Program_Phase_2</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="analog"
     data-types="Oscillator"
     data-proven="false"
     data-name="analog sky26a">
  <div class="card-header">
    <h3><a href="https://github.com/Essenceia/analog_sky26a" target="_blank" rel="noopener">Analog Sky26A</a></h3>
    
  </div>
  <p class="card-summary">Analog experiements, targetting sky26a, double oscillators</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">Oscillator</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Essenceia/analog_sky26a" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Essenceia/analog_sky26a</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="nasscom vsd soc">
  <div class="card-header">
    <h3><a href="https://github.com/arudeep15/NASSCOM-VSD-SOC" target="_blank" rel="noopener">Nasscom Vsd Soc</a></h3>
    
  </div>
  <p class="card-summary">This Repository consists of the learnings and simulations using OpenLANE under the workshop by VSD entitled as SOC Design and Planning Workshop.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/arudeep15/NASSCOM-VSD-SOC" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> arudeep15/NASSCOM-VSD-SOC</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="aurora v1">
  <div class="card-header">
    <h3><a href="https://github.com/kudumyashwanth/aurora-v1" target="_blank" rel="noopener">Aurora V1</a></h3>
    
  </div>
  <p class="card-summary">Aurora v1 — a complete RISC-V + tensor-accelerator AI SoC taken from RTL to signed-off GDSII with open-source tools (Sky130B). Timing MET, DRC=1, LVS device-match.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/kudumyashwanth/aurora-v1" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> kudumyashwanth/aurora-v1</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="digital"
     data-types="unknown"
     data-proven="true"
     data-name="systolic array with dft v2">
  <div class="card-header">
    <h3><a href="https://github.com/Essenceia/Systolic_Array_with_DFT_v2" target="_blank" rel="noopener">Systolic Array With Dft V2</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">IHP 130nm ASIC tapeout of a 2x2 bfloat16 matrix matrix multiplication with DFT infrastructure. Iteration on the previous accelerator taped out on GF180.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Essenceia/Systolic_Array_with_DFT_v2" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Essenceia/Systolic_Array_with_DFT_v2</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="ihp mcu2972">
  <div class="card-header">
    <h3><a href="https://github.com/CDTA-DMN/IHP__MCU2972" target="_blank" rel="noopener">Ihp Mcu2972</a></h3>
    
  </div>
  <p class="card-summary">An open-source 32-bit RISC-V MCU designed for IHP SG13G2 130nm BiCMOS technology. Features a PicoRV32 core, QSPI XIP, and a rich peripheral set for low-power IoT and embedded control.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/CDTA-DMN/IHP__MCU2972" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> CDTA-DMN/IHP__MCU2972</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="analog"
     data-types="VCO Oscillator"
     data-proven="false"
     data-name="current starved vco ihp">
  <div class="card-header">
    <h3><a href="https://github.com/Pa1mantri/Current_Starved_VCO_IHP" target="_blank" rel="noopener">Current Starved Vco Ihp</a></h3>
    
  </div>
  <p class="card-summary">Voltage Controlled Oscillator that produces 1GHz output frequency at voltage 3.3V using IHP PDK as a part of eSim Marathon</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">VCO, Oscillator</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Pa1mantri/Current_Starved_VCO_IHP" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Pa1mantri/Current_Starved_VCO_IHP</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="analog"
     data-types="LNA VCO Power Amplifier"
     data-proven="false"
     data-name="silicoweave mmwave ip">
  <div class="card-header">
    <h3><a href="https://github.com/OmarAlani1978/SilicoWeave-mmWave-IP" target="_blank" rel="noopener">Silicoweave Mmwave Ip</a></h3>
    
  </div>
  <p class="card-summary">Low-power mmWave IP portfolio on IHP SG13G2 SiGe BiCMOS — V-band LNA, VCO, and PA driver</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">LNA, VCO, Power Amplifier</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/OmarAlani1978/SilicoWeave-mmWave-IP" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> OmarAlani1978/SilicoWeave-mmWave-IP</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="globalfoundries pdk ip gf180mcu fd ip sram">
  <div class="card-header">
    <h3><a href="https://github.com/google/globalfoundries-pdk-ip-gf180mcu_fd_ip_sram" target="_blank" rel="noopener">Globalfoundries Pdk Ip Gf180Mcu Fd Ip Sram</a></h3>
    
  </div>
  <p class="card-summary">SRAM macros created for the GF180MCU provided by GlobalFoundries.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/google/globalfoundries-pdk-ip-gf180mcu_fd_ip_sram" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> google/globalfoundries-pdk-ip-gf180mcu_fd_ip_sram</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="digital"
     data-types="SRAM"
     data-proven="false"
     data-name="globalfoundries pdk libs gf180mcu fd bd sram">
  <div class="card-header">
    <h3><a href="https://github.com/google/globalfoundries-pdk-libs-gf180mcu_fd_bd_sram" target="_blank" rel="noopener">Globalfoundries Pdk Libs Gf180Mcu Fd Bd Sram</a></h3>
    
  </div>
  <p class="card-summary">SRAM build space for the GF180MCU provided by GlobalFoundries.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SRAM</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/google/globalfoundries-pdk-libs-gf180mcu_fd_bd_sram" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> google/globalfoundries-pdk-libs-gf180mcu_fd_bd_sram</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="unknown"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="gf180mcu kianv rv32ima sv32">
  <div class="card-header">
    <h3><a href="https://github.com/splinedrive/gf180mcu-kianv-rv32ima-sv32" target="_blank" rel="noopener">Gf180Mcu Kianv Rv32Ima Sv32</a></h3>
    
  </div>
  <p class="card-summary">KianV GF180 ASIC runs ulinux, linux and XV6</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/splinedrive/gf180mcu-kianv-rv32ima-sv32" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> splinedrive/gf180mcu-kianv-rv32ima-sv32</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="ethernet switch">
  <div class="card-header">
    <h3><a href="https://github.com/Essenceia/ethernet_switch" target="_blank" rel="noopener">Ethernet Switch</a></h3>
    
  </div>
  <p class="card-summary">Open source sillicon for a 100Mbps 3 port unmanaged cut-though ethernet switch</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Essenceia/ethernet_switch" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Essenceia/ethernet_switch</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="unknown"
     data-types="unknown"
     data-proven="true"
     data-name="wafer space docker based starter kit">
  <div class="card-header">
    <h3><a href="https://github.com/evezor/wafer_space_docker_based_starter_kit" target="_blank" rel="noopener">Wafer Space Docker Based Starter Kit</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">Beginner-friendly, Docker-based starter kit for designing a GF180MCU chip from RTL to a manufacturable GDSII — simulate, verify, and harden a working example, then make it yours and submit it to a wafer.space shuttle.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/evezor/wafer_space_docker_based_starter_kit" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> evezor/wafer_space_docker_based_starter_kit</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="verigpu">
  <div class="card-header">
    <h3><a href="https://github.com/hughperkins/VeriGPU" target="_blank" rel="noopener">Verigpu</a></h3>
    
  </div>
  <p class="card-summary">OpenSource GPU, in Verilog, loosely based on RISC-V ISA</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/hughperkins/VeriGPU" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> hughperkins/VeriGPU</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="cores veer eh1">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/Cores-VeeR-EH1" target="_blank" rel="noopener">Cores Veer Eh1</a></h3>
    
  </div>
  <p class="card-summary">VeeR EH1 core</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/Cores-VeeR-EH1" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/Cores-VeeR-EH1</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="cores veer el2">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/Cores-VeeR-EL2" target="_blank" rel="noopener">Cores Veer El2</a></h3>
    
  </div>
  <p class="card-summary">VeeR EL2 Core</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/Cores-VeeR-EL2" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/Cores-VeeR-EL2</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core SoC"
     data-proven="false"
     data-name="axi crossbar">
  <div class="card-header">
    <h3><a href="https://github.com/dpretet/axi-crossbar" target="_blank" rel="noopener">Axi Crossbar</a></h3>
    
  </div>
  <p class="card-summary">Parametric AXI4 crossbar in SystemVerilog</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/dpretet/axi-crossbar" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> dpretet/axi-crossbar</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="openasip">
  <div class="card-header">
    <h3><a href="https://github.com/cpc/openasip" target="_blank" rel="noopener">Openasip</a></h3>
    
  </div>
  <p class="card-summary">Open Application-Specific Instruction Set processor tools (OpenASIP)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/cpc/openasip" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> cpc/openasip</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor SoC"
     data-proven="false"
     data-name="design and asic implementation of 32 point fft processor">
  <div class="card-header">
    <h3><a href="https://github.com/abdelazeem201/Design-and-ASIC-Implementation-of-32-Point-FFT-Processor" target="_blank" rel="noopener">Design And Asic Implementation Of 32 Point Fft Processor</a></h3>
    
  </div>
  <p class="card-summary">I present a novel pipelined fast Fourier transform (FFT) architecture which is capable of producing the output sequence in normal order. A single-path delay commutator processing element (SDC PE) has been proposed for the first time. It saves a complex adder compared with the typical radix-2 butterfly unit. The new pipelined architecture can be built using the proposed processing element. The proposed architecture can lead to 100% hardware utilization and 50% reduction in the overall number of a</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/abdelazeem201/Design-and-ASIC-Implementation-of-32-Point-FFT-Processor" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> abdelazeem201/Design-and-ASIC-Implementation-of-32-Point-FFT-Processor</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="vlsi asic design flow">
  <div class="card-header">
    <h3><a href="https://github.com/VardhanSuroshi/VLSI-ASIC-Design-Flow" target="_blank" rel="noopener">Vlsi Asic Design Flow</a></h3>
    
  </div>
  <p class="card-summary">This repository is dedicated to VLSI ASIC Design Flow using open-source tools! Here, we embark on a journey that starts with specifications, RTL DV, Synthesis, Physical Design, Signoff and Finally Tape-It-Out</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/VardhanSuroshi/VLSI-ASIC-Design-Flow" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> VardhanSuroshi/VLSI-ASIC-Design-Flow</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="quasar">
  <div class="card-header">
    <h3><a href="https://github.com/Lampro-Mellon/Quasar" target="_blank" rel="noopener">Quasar</a></h3>
    
  </div>
  <p class="card-summary">Quasar 2.0: Chisel equivalent of SweRV-EL2</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Lampro-Mellon/Quasar" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Lampro-Mellon/Quasar</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core SoC"
     data-proven="false"
     data-name="friscv">
  <div class="card-header">
    <h3><a href="https://github.com/dpretet/friscv" target="_blank" rel="noopener">Friscv</a></h3>
    
  </div>
  <p class="card-summary">RISCV CPU implementation in SystemVerilog</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/dpretet/friscv" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> dpretet/friscv</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SERDES"
     data-proven="false"
     data-name="rtl to gds implementation of serdes">
  <div class="card-header">
    <h3><a href="https://github.com/meeeeet/RTL-to-GDS-Implementation-of-SerDes" target="_blank" rel="noopener">Rtl To Gds Implementation Of Serdes</a></h3>
    
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SERDES</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/meeeeet/RTL-to-GDS-Implementation-of-SerDes" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> meeeeet/RTL-to-GDS-Implementation-of-SerDes</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="rv32i pipeline processor">
  <div class="card-header">
    <h3><a href="https://github.com/arhamhashmi01/rv32i-pipeline-processor" target="_blank" rel="noopener">Rv32I Pipeline Processor</a></h3>
    
  </div>
  <p class="card-summary">This repository contain the implementaton of RV32I 5-Stage-Pipeline-Processor based on RISC-V ISA and designed on Verilog</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/arhamhashmi01/rv32i-pipeline-processor" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> arhamhashmi01/rv32i-pipeline-processor</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="unknown"
     data-types="Processor"
     data-proven="false"
     data-name="tpu.sv">
  <div class="card-header">
    <h3><a href="https://github.com/kagandikmen/TPU.sv" target="_blank" rel="noopener">Tpu.Sv</a></h3>
    
  </div>
  <p class="card-summary">Anatomy of a powerhouse: SystemVerilog TPU based on Google TPU v1</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/kagandikmen/TPU.sv" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> kagandikmen/TPU.sv</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="nasscom vsd soc design program">
  <div class="card-header">
    <h3><a href="https://github.com/AnoushkaTripathi/NASSCOM-VSD-SoC-design-Program" target="_blank" rel="noopener">Nasscom Vsd Soc Design Program</a></h3>
    
  </div>
  <p class="card-summary"> In this workshop, we will delve into the process of designing an Application Specific Integrated Circuit (ASIC) from the Register Transfer Level (RTL) to the Graphical Data System (GDS)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/AnoushkaTripathi/NASSCOM-VSD-SoC-design-Program" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> AnoushkaTripathi/NASSCOM-VSD-SoC-design-Program</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="risc v rtl2gdsii">
  <div class="card-header">
    <h3><a href="https://github.com/ShekharShwetank/RISC-V_RTL2GDSII" target="_blank" rel="noopener">Risc V Rtl2Gdsii</a></h3>
    
  </div>
  <p class="card-summary">Learning Path: RISC-V System-on-Chip (SoC) design, from Register Transfer Level (RTL) to a GDSII layout | Complete VLSI design flow using open-source EDA tools.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/ShekharShwetank/RISC-V_RTL2GDSII" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> ShekharShwetank/RISC-V_RTL2GDSII</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor SoC"
     data-proven="false"
     data-name="leon2">
  <div class="card-header">
    <h3><a href="https://github.com/abdelazeem201/LEON2" target="_blank" rel="noopener">Leon2</a></h3>
    
  </div>
  <p class="card-summary">The LEON2 is a synthesisable VHDL model of a 32-bit processor conforming to the IEEE-1754 (SPARC V8) architecture.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/abdelazeem201/LEON2" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> abdelazeem201/LEON2</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="DAC"
     data-proven="false"
     data-name="sv i2s rx core">
  <div class="card-header">
    <h3><a href="https://github.com/rubinsteina13/SV_I2S_RX_CORE" target="_blank" rel="noopener">Sv I2S Rx Core</a></h3>
    
  </div>
  <p class="card-summary">Synthesizable SystemVerilog IP-Core of the I2S Receiver</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">DAC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/rubinsteina13/SV_I2S_RX_CORE" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> rubinsteina13/SV_I2S_RX_CORE</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="voyager fds">
  <div class="card-header">
    <h3><a href="https://github.com/Zaneham/voyager-fds" target="_blank" rel="noopener">Voyager Fds</a></h3>
    
  </div>
  <p class="card-summary">The Voyager flight computer on SKY130 silicon. 58 cells. Currently 24 billion km away.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Zaneham/voyager-fds" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Zaneham/voyager-fds</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="verilog rtl coding">
  <div class="card-header">
    <h3><a href="https://github.com/Kethasriramya2912/Verilog-RTL-Coding" target="_blank" rel="noopener">Verilog Rtl Coding</a></h3>
    
  </div>
  <p class="card-summary">&quot;Mastering RTL-Coding : From Fundamentals to Advanced Programming Techniques using Verilog,System Verilog and UVM&quot;</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Kethasriramya2912/Verilog-RTL-Coding" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Kethasriramya2912/Verilog-RTL-Coding</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="npu">
  <div class="card-header">
    <h3><a href="https://github.com/Ammar-Wahidi/NPU" target="_blank" rel="noopener">Npu</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">Silicon-proven INT8 systolic NPU (8×8 MAC array) taped out on SkyWater 130nm via LibreLane. Features a custom 32-bit ISA, UART–APB host interface, and fused streaming datapath. Validated on chest X-ray pneumonia detection. Silicon Sprint 2026 — AUC.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Ammar-Wahidi/NPU" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Ammar-Wahidi/NPU</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="Processor Filter"
     data-proven="false"
     data-name="ruru">
  <div class="card-header">
    <h3><a href="https://github.com/Zaneham/ruru" target="_blank" rel="noopener">Ruru</a></h3>
    
  </div>
  <p class="card-summary">The world&#x27;s first probabilistic processor. Distributions are the data type. Bayesian inference is a machine instruction. 2,237 SKY130 gates.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, Filter</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Zaneham/ruru" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Zaneham/ruru</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="qsim">
  <div class="card-header">
    <h3><a href="https://github.com/Zaneham/qsim" target="_blank" rel="noopener">Qsim</a></h3>
    
  </div>
  <p class="card-summary">Quantum circuit accelerator on classical silicon. 8 qubits, 238 gates, 200MHz. Because irony is a valid design methodology.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Zaneham/qsim" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Zaneham/qsim</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core SoC"
     data-proven="false"
     data-name="tinymoa">
  <div class="card-header">
    <h3><a href="https://github.com/EzraWolf/TinyMOA" target="_blank" rel="noopener">Tinymoa</a></h3>
    
  </div>
  <p class="card-summary">LLM inference SoC</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/EzraWolf/TinyMOA" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> EzraWolf/TinyMOA</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="analog"
     data-types="Filter"
     data-proven="false"
     data-name="tste87">
  <div class="card-header">
    <h3><a href="https://github.com/mnemocron/TSTE87" target="_blank" rel="noopener">Tste87</a></h3>
    
  </div>
  <p class="card-summary">MATLAB code for the lab sessions in the &quot;ASIC for DSP&quot; course at LiU-ISY</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">Filter</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/mnemocron/TSTE87" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> mnemocron/TSTE87</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="evpix rv32">
  <div class="card-header">
    <h3><a href="https://github.com/aukhalid/evpix_rv32" target="_blank" rel="noopener">Evpix Rv32</a></h3>
    
  </div>
  <p class="card-summary">EVPIX-RV32: 5-Stage Custom RISC-V SoC with Integrated IPU and TinyML Support for Real-Time Edge-Vision AI Acceleration: RTL-to-GDSII Design, Verification, Basys-3 Artix-7 FPGA Prototyping and SkyWater 130-nm CMOS ASIC was implementation</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/aukhalid/evpix_rv32" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> aukhalid/evpix_rv32</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="false"
     data-name="advanced digital logic lib">
  <div class="card-header">
    <h3><a href="https://github.com/logicbyvini/advanced-digital-logic-lib" target="_blank" rel="noopener">Advanced Digital Logic Lib</a></h3>
    
  </div>
  <p class="card-summary">SystemVerilog ASIC Portfolio: RISC-V SoC Integration, UVM Verification, AI Accelerators &amp; DSP. Full Flow from RTL to GDSII (Cadence).</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/logicbyvini/advanced-digital-logic-lib" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> logicbyvini/advanced-digital-logic-lib</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="DAC"
     data-proven="false"
     data-name="sv dsm core">
  <div class="card-header">
    <h3><a href="https://github.com/rubinsteina13/SV_DSM_CORE" target="_blank" rel="noopener">Sv Dsm Core</a></h3>
    
  </div>
  <p class="card-summary">Synthesizable SystemVerilog IP-Core of the First-Order Delta-Sigma Modulator</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">DAC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/rubinsteina13/SV_DSM_CORE" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> rubinsteina13/SV_DSM_CORE</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="architectural design for bus interface connected with lfsr">
  <div class="card-header">
    <h3><a href="https://github.com/shahed22/Architectural-Design-for-Bus-interface-connected-with-LFSR" target="_blank" rel="noopener">Architectural Design For Bus Interface Connected With Lfsr</a></h3>
    
  </div>
  <p class="card-summary">bus interface, integrating LFSR’s for streamlined register management. Enabled seamless master-peripheral communication, enhancing system efficiency. Orchestrated comprehensive design stages, yielding a versatile RTL architecture for diverse applications</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/shahed22/Architectural-Design-for-Bus-interface-connected-with-LFSR" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> shahed22/Architectural-Design-for-Bus-interface-connected-with-LFSR</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="dlx processor portfolio">
  <div class="card-header">
    <h3><a href="https://github.com/SilviaB24/DLX-Processor-Portfolio" target="_blank" rel="noopener">Dlx Processor Portfolio</a></h3>
    
  </div>
  <p class="card-summary">Full RTL-to-GDSII implementation of a 32-bit RISC Processor. Features Physical Design (P&amp;R), CTS, and Timing Closure using Synopsys DC &amp; Cadence Innovus.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/SilviaB24/DLX-Processor-Portfolio" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> SilviaB24/DLX-Processor-Portfolio</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="unknown"
     data-types="unknown"
     data-proven="false"
     data-name="dozenal alu">
  <div class="card-header">
    <h3><a href="https://github.com/Zaneham/dozenal-alu" target="_blank" rel="noopener">Dozenal Alu</a></h3>
    
  </div>
  <p class="card-summary">Base-12 arithmetic in silicon. 182 SKY130 gates. The Mesopotamians were right.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/Zaneham/dozenal-alu" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> Zaneham/dozenal-alu</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="optical"
     data-types="SoC"
     data-proven="false"
     data-name="raven picorv32">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/raven-picorv32" target="_blank" rel="noopener">Raven Picorv32</a></h3>
    
  </div>
  <p class="card-summary">Silicon-validated SoC implementation of the PicoSoc/PicoRV32</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/raven-picorv32" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/raven-picorv32</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="raptor">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/raptor" target="_blank" rel="noopener">Raptor</a></h3>
    
  </div>
  <p class="card-summary">Arm Cortex-M0 based Customizable SoC for IoT Applications</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/raptor" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/raptor</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="ravenna">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/ravenna" target="_blank" rel="noopener">Ravenna</a></h3>
    
  </div>
  <p class="card-summary">32-bit RISC-V microcontroller</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/ravenna" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/ravenna</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="true"
     data-name="caravel ibex">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/caravel_ibex" target="_blank" rel="noopener">Caravel Ibex</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">An example project that utilizes caravel user space for an ibex based SoC</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/caravel_ibex" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/caravel_ibex</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="unknown"
     data-proven="false"
     data-name="foss asic tools">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/foss-asic-tools" target="_blank" rel="noopener">Foss Asic Tools</a></h3>
    
  </div>
  <p class="card-summary">FOSS-ASIC-TOOLS is all in one container for SKY130 based design both Analog and Digital. Below is a list of the current tools already installed and ready to use.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/foss-asic-tools" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/foss-asic-tools</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="caravel mgmt soc litex">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/caravel_mgmt_soc_litex" target="_blank" rel="noopener">Caravel Mgmt Soc Litex</a></h3>
    
  </div>
  <p class="card-summary">https://caravel-mgmt-soc-litex.readthedocs.io/en/latest/</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/caravel_mgmt_soc_litex" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/caravel_mgmt_soc_litex</a>
  </div>
</div>
<div class="design-card"
     data-pdk="skywater130"
     data-class="mixed-signal"
     data-types="SERDES"
     data-proven="false"
     data-name="openserdes">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/OpenSERDES" target="_blank" rel="noopener">Openserdes</a></h3>
    
  </div>
  <p class="card-summary">Digitally synthesizable architecture for SerDes using Skywater Open PDK 130 nm technology.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Skywater130</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">SERDES</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/OpenSERDES" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/OpenSERDES</a>
  </div>
</div>
<div class="design-card"
     data-pdk="gf180"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="caravel mgmt soc gf180mcu">
  <div class="card-header">
    <h3><a href="https://github.com/efabless/caravel_mgmt_soc_gf180mcu" target="_blank" rel="noopener">Caravel Mgmt Soc Gf180Mcu</a></h3>
    
  </div>
  <p class="card-summary">This repository is the GF180MCU port of management core for Caravel.  For more information about the Caravel management SoC, see https://github.com/efabless/caravel_mgmt_soc_litex.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Gf180</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/efabless/caravel_mgmt_soc_gf180mcu" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> efabless/caravel_mgmt_soc_gf180mcu</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="analog"
     data-types="Reference"
     data-proven="false"
     data-name="libkml">
  <div class="card-header">
    <h3><a href="https://github.com/google/libkml" target="_blank" rel="noopener">Libkml</a></h3>
    
  </div>
  <p class="card-summary">Reference implementation of OGC KML 2.2</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Analog</span>
    <span class="badge badge-type">Reference</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/google/libkml" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> google/libkml</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="rocket chip">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/rocket-chip" target="_blank" rel="noopener">Rocket Chip</a></h3>
    
  </div>
  <p class="card-summary">Rocket Chip Generator</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/rocket-chip" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/rocket-chip</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="riscv dv">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/riscv-dv" target="_blank" rel="noopener">Riscv Dv</a></h3>
    
  </div>
  <p class="card-summary">Random instruction generator for RISC-V processor verification</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/riscv-dv" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/riscv-dv</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="veerwolf">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/VeeRwolf" target="_blank" rel="noopener">Veerwolf</a></h3>
    
  </div>
  <p class="card-summary">FuseSoC-based SoC for VeeR EH1 and EL2</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/VeeRwolf" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/VeeRwolf</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="surelog">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/Surelog" target="_blank" rel="noopener">Surelog</a></h3>
    
  </div>
  <p class="card-summary">SystemVerilog 2017 Pre-processor, Parser, Elaborator, UHDM Compiler. Provides IEEE Design/TB C/C++ VPI and Python AST &amp; UHDM APIs. Compiles on Linux gcc, Windows msys2-gcc &amp; msvc, OsX </p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/Surelog" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/Surelog</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="dromajo">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/dromajo" target="_blank" rel="noopener">Dromajo</a></h3>
    
  </div>
  <p class="card-summary">RISC-V RV64GC emulator designed for RTL co-simulation</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/dromajo" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/dromajo</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="riscv v spec">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/riscv-v-spec" target="_blank" rel="noopener">Riscv V Spec</a></h3>
    
  </div>
  <p class="card-summary">Working draft of the proposed RISC-V V vector extension</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/riscv-v-spec" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/riscv-v-spec</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="false"
     data-name="cores swerv support package">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/Cores-SweRV-Support-Package" target="_blank" rel="noopener">Cores Swerv Support Package</a></h3>
    
  </div>
  <p class="card-summary">Processor support packages</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/Cores-SweRV-Support-Package" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/Cores-SweRV-Support-Package</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="SoC"
     data-proven="false"
     data-name="caravel swerv el2">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/caravel-swerv-el2" target="_blank" rel="noopener">Caravel Swerv El2</a></h3>
    
  </div>
  <p class="card-summary">Caravel is a standard SoC hardness with on chip resources to control and read/write operations from a user-dedicated space.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/caravel-swerv-el2" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/caravel-swerv-el2</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor RISC-V Core"
     data-proven="false"
     data-name="riscv fw infrastructure">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/riscv-fw-infrastructure" target="_blank" rel="noopener">Riscv Fw Infrastructure</a></h3>
    
  </div>
  <p class="card-summary">SDK Firmware infrastructure, contain RTOS Abstraction Layer, demos, SweRV Processor Support Package, and more ...</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor, RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/riscv-fw-infrastructure" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/riscv-fw-infrastructure</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="riscv vector tests">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/riscv-vector-tests" target="_blank" rel="noopener">Riscv Vector Tests</a></h3>
    
  </div>
  <p class="card-summary">Unit tests generator for RVV 1.0</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/riscv-vector-tests" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/riscv-vector-tests</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="RISC-V Core"
     data-proven="false"
     data-name="rvdecoderdb">
  <div class="card-header">
    <h3><a href="https://github.com/chipsalliance/rvdecoderdb" target="_blank" rel="noopener">Rvdecoderdb</a></h3>
    
  </div>
  <p class="card-summary">The Scala parser to parse riscv/riscv-opcodes generate</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/chipsalliance/rvdecoderdb" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> chipsalliance/rvdecoderdb</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="mixed-signal"
     data-types="Frequency Divider"
     data-proven="true"
     data-name="tinytapeout frequency div">
  <div class="card-header">
    <h3><a href="https://github.com/TinyTapeout/tinytapeout_frequency_div" target="_blank" rel="noopener">Tinytapeout Frequency Div</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">frequency divider tiny tapeout design</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Mixed Signal</span>
    <span class="badge badge-type">Frequency Divider</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/TinyTapeout/tinytapeout_frequency_div" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> TinyTapeout/tinytapeout_frequency_div</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="true"
     data-name="tinytapeout bintristateloadablecounter">
  <div class="card-header">
    <h3><a href="https://github.com/TinyTapeout/tinytapeout_bintristateloadablecounter" target="_blank" rel="noopener">Tinytapeout Bintristateloadablecounter</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">This IP block simulates a binary synchronous (parallel) MOD-4 counter. Applications are CPU&#x27;s, PWM signal generators, etc. It features:  - tri-direction (pause, count up, count down)  - loadable (use data[3:1], eg. for jump instruction) - synchronous output(at rising edge) with async (ripple) setup of next count)  - easy to control, fast and scalable (each 1 bit counter only depends on previous counter)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/TinyTapeout/tinytapeout_bintristateloadablecounter" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> TinyTapeout/tinytapeout_bintristateloadablecounter</a>
  </div>
</div>
<div class="design-card"
     data-pdk="unknown"
     data-class="digital"
     data-types="Processor"
     data-proven="true"
     data-name="tinytapeout mcpu5">
  <div class="card-header">
    <h3><a href="https://github.com/TinyTapeout/tinytapeout_mcpu5" target="_blank" rel="noopener">Tinytapeout Mcpu5</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">8 bit CPU optimized for the constraints of tinytapeout</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Unknown</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">Processor</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/TinyTapeout/tinytapeout_mcpu5" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> TinyTapeout/tinytapeout_mcpu5</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="lna 24ghz">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Dec2023/tree/main/LNA_24GHz" target="_blank" rel="noopener">Lna 24Ghz</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Dec2023/tree/main/LNA_24GHz" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/LNA_24GHz</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="y0 opensource lna">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Dec2023/tree/main/Y0_openSource_LNA" target="_blank" rel="noopener">Y0 Opensource Lna</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Dec2023/tree/main/Y0_openSource_LNA" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/Y0_openSource_LNA</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="unknown"
     data-types="LDO"
     data-proven="true"
     data-name="analogldo exampledesign">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/AnalogLDO_exampleDesign" target="_blank" rel="noopener">Analogldo Exampledesign</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">&gt; © Daniel Arevalos, Innovations for High Performance Microelectronics (IHP).</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Unknown</span>
    <span class="badge badge-type">LDO</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/AnalogLDO_exampleDesign" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/AnalogLDO_exampleDesign</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="digital"
     data-types="RISC-V Core SoC"
     data-proven="true"
     data-name="basilisk">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/Basilisk" target="_blank" rel="noopener">Basilisk</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">Basilisk is a tapeout of [Cheshire-IHP130-o](https://github.com/pulp-platform/cheshire-ihp130-o) which is an implementation of the [Cheshire SoC platform](https://github.com/pulp-platform/cheshire) in IHP130 using only open-source tools from RTL to GDS.</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Digital</span>
    <span class="badge badge-type">RISC-V Core, SoC</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/Basilisk" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/Basilisk</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="elemrv">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/ElemRV" target="_blank" rel="noopener">Elemrv</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/ElemRV" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/ElemRV</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="LDO"
     data-proven="true"
     data-name="u hawaii ee628 spring 2024">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/U_Hawaii_EE628_Spring_2024" target="_blank" rel="noopener">U Hawaii Ee628 Spring 2024</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">EE 628 (University of Hawaiʻi at Mānoa)  
https://github.com/bmurmann/EE628</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">LDO</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/U_Hawaii_EE628_Spring_2024" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/U_Hawaii_EE628_Spring_2024</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="ts pr may2024">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/ts_pr_May2024" target="_blank" rel="noopener">Ts Pr May2024</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_May2024/tree/main/ts_pr_May2024" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/ts_pr_May2024</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="ac3e usm tdbuck">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/AC3E_USM_TDBUCK" target="_blank" rel="noopener">Ac3E Usm Tdbuck</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/AC3E_USM_TDBUCK" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/AC3E_USM_TDBUCK</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="bg">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/BG" target="_blank" rel="noopener">Bg</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/BG" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/BG</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="chipchile canelos24 workshopto">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/CHIPCHILE_CANELOS24_WorkshopTO" target="_blank" rel="noopener">Chipchile Canelos24 Workshopto</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/CHIPCHILE_CANELOS24_WorkshopTO" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/CHIPCHILE_CANELOS24_WorkshopTO</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="cryochip">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/CryoChip" target="_blank" rel="noopener">Cryochip</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/CryoChip" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/CryoChip</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="differntial amp">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/Differntial_Amp" target="_blank" rel="noopener">Differntial Amp</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/Differntial_Amp" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/Differntial_Amp</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="exampledesign">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/ExampleDesign" target="_blank" rel="noopener">Exampledesign</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/ExampleDesign" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/ExampleDesign</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="flowspace srambitcelltest">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/FlowSpace_SRAMBitCellTest" target="_blank" rel="noopener">Flowspace Srambitcelltest</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary">See [doc/README.md](doc/README.md)</p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/FlowSpace_SRAMBitCellTest" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/FlowSpace_SRAMBitCellTest</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="martin">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/MARTIn" target="_blank" rel="noopener">Martin</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/MARTIn" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/MARTIn</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="maskedandunmaskedaes">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/MaskedAndUnmaskedAES" target="_blank" rel="noopener">Maskedandunmaskedaes</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/MaskedAndUnmaskedAES" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/MaskedAndUnmaskedAES</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="arlet6502">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/arlet6502" target="_blank" rel="noopener">Arlet6502</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/arlet6502" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/arlet6502</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="GPIO"
     data-proven="true"
     data-name="i2c gpio expander">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/i2c-gpio-expander" target="_blank" rel="noopener">I2C Gpio Expander</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">GPIO</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/i2c-gpio-expander" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/i2c-gpio-expander</a>
  </div>
</div>
<div class="design-card"
     data-pdk="ihp130sg"
     data-class="optical"
     data-types="unknown"
     data-proven="true"
     data-name="sg13g2 io testchip">
  <div class="card-header">
    <h3><a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/sg13g2_io_testchip" target="_blank" rel="noopener">Sg13G2 Io Testchip</a></h3>
    <span class="badge badge-proven">Silicon Proven</span>
  </div>
  <p class="card-summary"></p>
  <div class="card-badges">
    <span class="badge badge-pdk">Ihp130Sg</span>
    <span class="badge badge-class">Optical</span>
    <span class="badge badge-type">unknown</span>
  </div>
  
  <div class="card-footer">
    <a href="https://github.com/IHP-GmbH/TO_Nov2024/tree/main/sg13g2_io_testchip" target="_blank" rel="noopener" class="card-link"><svg viewBox="0 0 16 16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg> IHP-GmbH/sg13g2_io_testchip</a>
  </div>
</div>
</div>
