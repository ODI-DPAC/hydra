---
title: "Hydra Cluster Evolution: Complete History (2020-2024)"
date: 2026-09-16
author: "Compiled from what-s-new documentation"
---

# Hydra Cluster Evolution: Complete History (2020-2024)

## Timeline Overview

```
2020                  2021                  2022                  2023                  2024
 |                     |                     |                     |                     |
 ├─ DOI Setup          ├─ Major Upgrade      ├─ Storage/HW        ├─ Rocky 8 Planning   ├─ Rocky 8 Deployment
 ├─ GPFS Roadmap       ├─ Capacity +31%      │  Refresh            ├─ SW Updates        ├─ New Interactive Tools
 └─ Telework Access    └─ New Compilers      └─ New Nodes (21)     └─ 15 New Nodes       └─ WeTTY Interface
                                                                       Planned            └─ Additional GPU/Memory
```

---

## Detailed History by Year

### 2020: Foundation & Telework Readiness

| Date | Milestone | Details |
|------|-----------|---------|
| **Jan 14** | Increased Capacity | CPU slot limit raised from 512 to 640 cores per user |
| **Feb 27** | New CPU Architecture Resource | Added `cpu_arch` resource to direct jobs to specific CPU types; IDL 8.7.3 installed |
| **Mar 24** | Telework Support | Remote access infrastructure established; modified scrubbing policy (21-day retention) |
| **Apr 3** | DOI Registration | Hydra assigned [DOI: 10.25572/SIHPC](https://doi.org/10.25572/SIHPC) for research citations |
| **Sep 15** | GPFS & Software Upgrades | GPFS v4→v5 migration (rolling upgrade); IDL v8.8.0 released |

**Key Achievement**: Established remote access infrastructure and began modernization roadmap.

---

### 2021: Major Cluster Upgrade

| Date | Milestone | Details |
|------|-----------|---------|
| **Jun 24** | Upgrade Announcement | Major upgrade planned for Aug 30 – Sep 14 |
| **Sep 14** | Upgrade Completed | System reconfigured with backward compatibility prioritized |
| **Sep 25** | IDL Licensing Update | IDL 8.8.1 released; licensing method modernized |
| **Nov 22** | Software & Compiler Updates | Multiple new compiler versions; updated documentation |
| **Nov 29** | Module Defaults Updated | 7 module default versions updated per announcement |
| **Dec 2** | Hardware Delivery | 8 new servers + 56 GPFS disks received for deployment |
| **Dec 17** | Capacity Expansion | +8 compute nodes added: **5,408 CPUs across 98 nodes, 42TB memory** |

**Key Achievement**: Significant cluster expansion (+31% CPU capacity) with performance infrastructure improvements.

---

### 2022: Storage Modernization & Hardware Refresh

| Date | Milestone | Details |
|------|-----------|---------|
| **May 9** | Latest Compilers & Tools | NVIDIA 22.x, Intel 2022.x, IDL 8.2.2, MATLAB R2022a installed |
| **Nov 7** | Compute Node Refresh | +21 new compute nodes (Dell R6515, 64-core AMD EPYC, 512GB memory each) |
| **Nov 7** | Node Retirement | All old compute-81-xx (Dell R815) nodes retired |
| **Nov 15** | Storage Upgrade Completed | /home & /share/apps migrated to hybrid SSD/HDD aggregate for faster I/O |

**Key Achievement**: Storage performance doubled with hybrid disk technology; heterogeneous CPU architecture support matured.

---

### 2023: OS Modernization Planning & Software Expansion

| Date | Milestone | Details |
|------|-----------|---------|
| **Sep 27** | Software Stack Expansion | Python 3.11, IDL 8.9.0, MATLAB R2023a/b, Julia 1.9.3, NVIDIA 23.x installed |
| **Sep 27** | OS Migration Roadmap | CentOS 7 → Rocky 8 transition planned for Jan/Feb 2024 (10-day downtime expected) |
| **Nov 27** | Hardware Procurement | FY23 purchases approved: +15 new compute nodes (Zen4 CPUs, up to 192 cores), +1 quad-GPU server (A100s) |
| **Nov 27** | Personnel Transition | Rebecca Dikow transitioned after 7+ years; consolidated communications via si-hpc@si.edu |

**Key Achievement**: Prepared for major OS upgrade; expanded GPU capabilities and modern CPU support.

---

### 2024: OS Modernization & Modern Developer Tools

| Date | Milestone | Details |
|------|-----------|---------|
| **May 7** | Rocky 8.9 Deployment | Successfully migrated from CentOS 7.9; +15 new compute nodes added |
| **May 7** | New Compute Nodes** | 2× 192-CPU nodes (1.5TB RAM), 12× 128-CPU nodes (1TB RAM), 1× 4-GPU node (NVIDIA L40S) |
| **Jun 6** | Tooling Updates | Dropbox uploader deprecated; IDL license server relocated to hydra-7 |
| **Jul 15** | Browser-Based Development Environments | JupyterLab, RStudio (v4.4.1), and VSCode scripts deployed |
| **Sep 6** | Maintenance Window | 3-day shutdown for system maintenance |
| **Sep 16** | Compiler & Tool Updates | GNU 14.2.0, NVIDIA 24.3/24.5, Intel 2024.1/2024.2, awscli 2.17.43, gnuplot on all nodes |
| **Sep 16** | Memory Expansion | 1× compute node with 3TB memory added to ultra-large memory queue |
| **Sep 16** | DNS Aliasing | `hydra.si.edu` now points to latest version (hydra-7.si.edu) |
| **Oct 26** | User Communication | Automated email notification system documented |
| **Oct 28** | New Web Interface | WeTTY (web-based SSH terminal) launched; shell-in-a-box deprecated (sunset Dec 1) |
| **Nov 7** | Workflow Management | New "WFM" special queue for workflow managers; `dos2unix` utility added |
| **Nov 22** | Latest MATLAB | MATLAB R2024a & R2024b released |

**Key Achievement**: Transitioned to modern OS foundation; deployed state-of-the-art interactive development platforms.

---

## Summary: Key Metrics Over Time

### CPU Capacity Growth
- **Jan 2020**: 512 slots (user limit)
- **Jan 2022**: 840 slots (64% increase)
- **Dec 2021**: 5,408 CPUs (98 nodes)
- **May 2024**: ~6,600 CPUs after Zen4 additions (~22% growth)

### Storage Evolution
- **2020-2021**: GPFS v4 → v5 migration
- **Nov 2022**: Hybrid SSD/HDD aggregate for /home & /share/apps
- **2024+**: Planned expansion of /scratch and high-speed storage

### GPU Capabilities
- **2023**: Planned quad-GPU server (A100s)
- **2024**: Deployed 1× L40S quad-GPU node

### Operating System & Software Stack
- **2021**: Compilers & tools modernized
- **2024**: Rocky 8.9 deployed; modern developer tools integrated
- **Latest**: GNU 14.2, NVIDIA 24.x, Intel 2024.x compilers available

### User Experience Improvements
- **2020-2021**: Remote access via VPN/RDP
- **2024**: WeTTY modern web terminal; browser-based JupyterLab, RStudio, VSCode

---

## Key Architectural Milestones

### Phase 1: Remote-Ready Foundation (2020-2021)
- Established hybrid cloud-ready infrastructure
- GPFS modernization
- Initial capacity growth to 5,408 CPUs

### Phase 2: Specialized Hardware (2022-2023)
- Heterogeneous CPU architecture (Zen, Zen2, Zen4)
- Hybrid storage for performance-critical filesystems
- GPU support introduction
- Preparation for OS modernization

### Phase 3: Modern Platform (2024+)
- Rocky 8 foundation (RHEL 9-compatible)
- Cutting-edge CPU/compiler support
- Browser-based scientific computing workflows
- Scalable interactive development environments

---

## Policy & Access Changes

| Year | Change | Impact |
|------|--------|--------|
| 2020 | Scrubbing policy modified (21-day retention) | User data protection improved |
| 2021-2022 | CPU slot limits increased (512→840) | Larger jobs supported |
| 2023-2024 | /data access expanded (up to 2TB storage) | Genomics & SAO research enabled |
| 2024 | Workflow manager queue added | Complex pipeline execution |

---

## Looking Forward

Based on 2024 announcements:
- **Storage**: Planned expansion of /scratch and fast-tier storage
- **Compute**: Further CPU density optimization
- **Accessibility**: Modern web interfaces maturing
- **Software**: Continuous compiler & tool updates following vendor releases
- **Stability**: OS upgrade cycle established (CentOS 7 → Rocky 8 pattern)

---

*Last Updated: December 2024 | Data compiled from official Hydra documentation*
