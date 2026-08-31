# Awesome Object Counting

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/github/license/Mengqi-Lei/awesome-object-counting)](LICENSE)

A curated collection of research on visual object counting, including papers, datasets, benchmarks, leaderboards, tutorials, and project resources.

> **Collection policy.** For work published in 2022 or earlier, we retain seminal and broadly recognized papers. From 2023 onward, we aim for high recall across major conferences, reputable journals, and verifiable arXiv papers, provided that object counting is a central contribution.

Metadata last verified: **2026-08-31**.

## Contents

- [What is Object Counting?](#what-is-object-counting)
- [Task Taxonomy](#task-taxonomy)
- [Highlights](#highlights)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Papers](#papers)
  - [Open-vocabulary Counting](#open-vocabulary-counting)
  - [Exemplar-based Counting](#exemplar-based-counting)
  - [MLLM-based Counting](#mllm-based-counting)
  - [Class-agnostic Counting](#class-agnostic-counting)
  - [Class-specific Counting](#class-specific-counting)
  - [Video Object Counting](#video-object-counting)
- [Leaderboard](#leaderboard)
  - [FSC-147](#fsc-147)
  - [CLOC](#cloc)
- [Tutorials and Blogs](#tutorials-and-blogs)
- [Contributing](#contributing)

## What is Object Counting?

Object counting estimates how many instances of a target concept appear in an image or video. Depending on the setting, the target may be fixed during training, specified by visual exemplars, described in natural language, or inferred by a multimodal large language model. Methods may predict a scalar count, density map, point set, or detected instances.

## Task Taxonomy

The taxonomy is intentionally multi-label: a paper can appear in more than one section when it combines, for example, open-vocabulary language prompts with class-agnostic counting.

1. **Open-vocabulary Counting** — specifies the target with unrestricted or open-set natural-language concepts.
2. **Exemplar-based Counting** — specifies the target using boxes, points, crops, or reference images.
3. **MLLM-based Counting** — studies counting through multimodal large language models, including direct answers, reasoning, grounding, or tool use.
4. **Class-agnostic Counting** — counts arbitrary or previously unseen categories rather than a fixed training class.
5. **Class-specific Counting** — specializes in a known semantic class or application domain, such as crowds, vehicles, cells, crops, or industrial objects.
6. **Video Object Counting** — counts objects in videos while addressing temporal consistency, motion, recurrence, or tracking.

## Highlights

- **[Count Anything]** Count Anything. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.30846)] [[Code](https://github.com/Mengqi-Lei/count-anything)]
- **[CountGD++]** CountGD++: Generalized Prompting for Open-World Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Amini-Naieni_CountGD_Generalized_Prompting_for_Open-World_Counting_CVPR_2026_paper.html)] [[Code](https://github.com/niki-amini-naieni/CountGDPlusPlus)]
- **[CountVid]** Open-World Object Counting in Videos. (**AAAI 2026**) [[Paper](https://arxiv.org/abs/2506.15368)] [[Code](https://github.com/niki-amini-naieni/CountVid)]
- **[UNICBench]** UNICBench: UNIfied Counting Benchmark for MLLM. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rong_UNICBench_UNIfied_Counting_Benchmark_for_MLLM_CVPR_2026_paper.html)]
- **[T2ICount]** T2ICount: Enhancing Cross-Modal Understanding for Zero-Shot Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_T2ICount_Enhancing_Cross-modal_Understanding_for_Zero-Shot_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/cha15yq/T2ICount)]
- **[GeCo]** A Novel Unified Architecture for Low-Shot Counting by Detection and Segmentation. (**NeurIPS 2024**) [[Paper](https://arxiv.org/abs/2409.18686)] [[Code](https://github.com/jerpelhan/GeCo)]
- **[CountGD]** CountGD: Multi-Modal Open-World Counting. (**NeurIPS 2024**) [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html)] [[Code](https://github.com/niki-amini-naieni/CountGD)]
- **[CLIP-Count]** CLIP-Count: Towards Text-Guided Zero-Shot Object Counting. (**ACM MM 2023**) [[Paper](https://arxiv.org/abs/2305.07304)] [[Code](https://github.com/songrise/CLIP-Count)]
- **[FamNet]** Learning To Count Everything. (**CVPR 2021**) [[Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.html)] [[Code](https://github.com/cvlab-stonybrook/LearningToCountEverything)]
- **[GMN]** Class-Agnostic Counting. (**ACCV 2018**) [[Paper](https://ora.ox.ac.uk/objects/uuid%3A0700b0af-1b14-4f4e-a7bc-8f38e93b4a51)]
- **[MCNN]** Single-Image Crowd Counting via Multi-Column Convolutional Neural Network. (**CVPR 2016**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2016/html/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.html)]
- **[Lempitsky et al.]** Learning To Count Objects in Images. (**NeurIPS 2010**) [[Paper](https://proceedings.neurips.cc/paper/2010/hash/fe73f687e5bc5280214e0486b273a5f9-Abstract.html)] [[Code](https://robots.ox.ac.uk/~vgg/research/counting/index.html)]

## Datasets and Benchmarks

The catalog currently contains **64** datasets and benchmarks: **52 verified** entries and **12 candidates** whose metadata is still being completed. See [data/datasets.csv](data/datasets.csv) for task, modality, scale, annotations, access, license, status, and source fields.

Candidate rows are deliberately marked below and should not be treated as fully verified releases.

<details>
<summary><b>Full dataset catalog (64 entries)</b></summary>

| Year | Dataset | Domain | Scale | Annotations | Links | Status |
|---:|---|---|---|---|---|---|
| 2026 | **CLOC** | general;remote sensing;histopathology;cellular microscopy;agriculture;microbiology | about 220K images;15.356M instances | unified points;source-dependent boxes/masks/polygons before conversion;text queries | [[Paper](https://arxiv.org/abs/2605.30846)] [[Project](https://mengqi-lei.github.io/count-anything-projectpage/)] [[Download](https://github.com/Mengqi-Lei/count-anything/tree/main/data)] | Verified |
| 2026 | **EC-Bench** | documentary;sports;news;TV;live;cartoon;academic | 152 videos longer than 30 minutes;1,699 queries | enumerated instances;integer counts;explicit evidence spans | [[Paper](https://arxiv.org/abs/2603.29943)] | Verified |
| 2026 | **GROC** | remote sensing | about 14,000 images;about 1.2M point annotations | points;geospatial metadata;aligned auxiliary modalities | [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_See_What_We_Cannot_See_A_Geo-guided_Reasoning_Benchmark_for_CVPR_2026_paper.html)] | Verified |
| 2026 | **HoloCount** | general scene | 2,480 QA pairs | questions;integer answers;20 task labels;difficulty/robustness categories | [[Paper](https://arxiv.org/abs/2607.06420)] [[Project](https://mm-mvr.github.io/HoloCount/)] [[Download](https://github.com/MM-MVR/HoloCount)] | Verified |
| 2026 | **KubriCount** | general synthetic scene | unknown | instance masks/locations;identity;attribute;type/category/concept granularity;positive and negative prompts | [[Paper](https://arxiv.org/abs/2605.10887)] [[Project](https://verg-avesta.github.io/KubriCount/)] | Candidate |
| 2026 | **MixCount** | general;industrial inspection;product sorting | 58,100 scenes;over 4M instances | instance/class masks;boxes;counts;depth;normals;text descriptions;internal/external exemplars | [[Paper](https://arxiv.org/abs/2605.18063)] [[Project](https://corentindumery.github.io/projects/mixcount.html)] [[Download](https://huggingface.co/datasets/CorentinDumery/MixCount)] | Verified |
| 2026 | **MUCCA** | general real-world scenes | 200 real-world images | multi-category points/counts;text prompts | [[Paper](https://arxiv.org/abs/2605.02752)] | Candidate |
| 2026 | **OCCAM Synthetic Multi-Class** | general synthetic scene | unknown | instance/class labels;per-class counts | [[Paper](https://arxiv.org/abs/2601.13871)] [[Project](https://mikespanak.github.io/OCCAM_counter)] | Candidate |
| 2026 | **PrACo++** | general scene | evaluation suite over existing counting datasets plus MUCCA | positive/negative prompts;distractor composition;specialized grounding metrics | [[Paper](https://arxiv.org/abs/2605.02752)] | Verified |
| 2026 | **SVCBench** | general dynamic scenes | unknown | streaming queries;state updates;counts;temporal evidence | [[Paper](https://arxiv.org/abs/2603.12703)] [[Project](https://buaa-colalab.github.io/SVCBench/)] | Candidate |
| 2026 | **TPC-268** | agriculture;botany;remote sensing;microscopy | 10,000 images;678,050 point annotations | points;Linnaean taxonomy;organ labels;scale-aware splits | [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Plant_Taxonomy_Meets_Plant_Counting_A_Fine-Grained_Taxonomic_Dataset_for_CVPR_2026_paper.html)] [[Project](https://github.com/tiny-smart/TPC-268)] [[Download](https://huggingface.co/datasets/jinyu-xu/TPC-268)] | Verified |
| 2026 | **UNICBench** | general multimodal | 5,300 images / 5,508 image QA;872 documents / 5,888 text QA;2,069 audio clips / 2,905 audio QA | questions;numeric answers;evidence-first ground truth;difficulty and capability tags | [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rong_UNICBench_UNIfied_Counting_Benchmark_for_MLLM_CVPR_2026_paper.html)] | Verified |
| 2026 | **VideoCount** | general;crowd;animal;materials | unknown | track identities;instance masks/boxes;video-level unique counts;text and visual prompts | [[Paper](https://www.robots.ox.ac.uk/~vgg/publications/2026/AminiNaieni26/)] [[Project](https://www.robots.ox.ac.uk/~vgg/research/countvid/)] | Candidate |
| 2025 | **3D Counting Dataset** | industrial;containers;stacked products | 400,000 synthetic images from 14,000 scenes;45 real scenes | ground-truth counts;3D meshes;volume occupancy;camera geometry | [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Dumery_Counting_Stacked_Objects_ICCV_2025_paper.html)] [[Project](https://corentindumery.github.io/projects/stacks.html)] | Verified |
| 2025 | **CAPTURe** | occluded patterned scenes | 2,212 released records across real and synthetic splits | image;occluder;counting question;integer answer;pattern metadata | [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Pothiraj_CAPTURE_Evaluating_Spatial_Reasoning_in_Vision_Language_Models_via_Occluded_ICCV_2025_paper.html)] [[Project](https://github.com/atinpothiraj/CAPTURe)] [[Download](https://huggingface.co/datasets/atinp/CAPTURe)] | Verified |
| 2025 | **CARPK-OCC** | vehicle;parking lots | derived from CARPK; exact released size unknown | original boxes/counts plus synthetic occluders and occlusion metadata | [[Paper](https://arxiv.org/abs/2511.12702)] | Candidate |
| 2025 | **CG-AV-Counting** | general long-form video | 497 long videos;1,027 questions;5,845 annotated clues | question;answer;temporal visual/audio clues;reasoning evidence | [[Paper](https://arxiv.org/abs/2506.05328)] [[Project](https://av-reasoner.github.io/)] [[Download](https://github.com/AV-Reasoner/AV-Reasoner)] | Verified |
| 2025 | **CountQA** | general real-world scenes | 1,001 released image records; over 1,500 QA pairs | questions;answers;object labels;scene categories;focused flag | [[Paper](https://arxiv.org/abs/2508.06585)] [[Project](https://research.google/pubs/countqa-how-well-do-mllms-count-in-the-wild/)] [[Download](https://huggingface.co/datasets/Jayant-Sravan/CountQA)] | Verified |
| 2025 | **DroneBird** | wildlife;natural scenes | 50 videos;about 21,500 benchmark frames | point annotations;density maps;trajectory annotations | [[Paper](https://openreview.net/forum?id=sY3anJ8C68)] [[Project](https://github.com/mast1ren/E-MAC)] | Verified |
| 2025 | **FSC-147-OCC** | general scene | derived from FSC-147; exact released size unknown | original points/counts plus synthetic occluders and occlusion metadata | [[Paper](https://arxiv.org/abs/2511.12702)] | Candidate |
| 2025 | **LOCO** | industrial;agriculture;daily life | unknown | point annotations;bounding boxes;counts | [[Paper](https://doi.org/10.1016/j.neunet.2025.107961)] [[Project](https://github.com/imMid-Star/CACAL)] | Candidate |
| 2025 | **MovingDroneCrowd** | dense crowd;drone | 89 clips;4,940 frames;325,541 head boxes;16,154 tracklets | head boxes;cross-frame identity IDs;inflow/outflow labels | [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Video_Individual_Counting_for_Moving_Drones_ICCV_2025_paper.html)] [[Project](https://github.com/fyw1999/MovingDroneCrowd)] | Verified |
| 2025 | **OmniCount-191** | general scene | 30,230 images;302,300 instances | points;boxes;category counts;VQA annotations | [[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/34151/36306)] [[Project](https://mondalanindya.github.io/OmniCount)] [[Download](https://huggingface.co/datasets/cvssp/OmniCount-191)] | Verified |
| 2025 | **PairTally** | paired-category scenes | 681 images | category-specific counts;fine-grained positive/negative prompts;paired distractor categories | [[Paper](https://arxiv.org/abs/2509.13939)] | Verified |
| 2025 | **PrACo** | general scene | derived test suite over FSC-147; no independent image corpus | positive/negative prompts; positive-label and negative-label tests; prompt-aware metrics | [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Ciampi_Mind_the_Prompt_A_Novel_Benchmark_for_Prompt-Based_Class-Agnostic_Counting_WACV_2025_paper.html)] [[Project](https://github.com/ciampluca/PrACo)] | Verified |
| 2024 | **CountBenchQA** | general scene | 491 currently packaged images from the original 540 CountBench entries | manually generated question;integer answer | [[Paper](https://arxiv.org/abs/2407.07726)] [[Project](https://github.com/google-research/big_vision/tree/main/big_vision/datasets/countbenchqa)] | Verified |
| 2024 | **MCAC** | general synthetic scene | 9,283 images;16,224 class-count records | center points;boxes;instance/class/model IDs;occlusion percentage;counts | [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01761.pdf)] [[Project](https://mcac.active.vision/)] | Verified |
| 2024 | **NWPU-MOC** | remote sensing | unknown | JSON instance annotations;density/count ground truth | [[Paper](https://doi.org/10.1109/TGRS.2024.3356492)] [[Project](https://github.com/lyongo/NWPU-MOC)] | Candidate |
| 2024 | **PixMo-Count** | general scene | 36,916 train records;540 validation;540 test;URLs may repeat | object label;integer count;training-set points;image SHA-256 | [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Deitke_Molmo_and_PixMo_Open_Weights_and_Open_Data_for_State-of-the-Art_CVPR_2025_paper.html)] [[Project](https://huggingface.co/datasets/allenai/pixmo-count)] | Verified |
| 2024 | **UpCount** | crowd;remote sensing | unknown | point annotations | [[Paper](https://arxiv.org/abs/2502.04014)] [[Project](https://zenodo.org/records/12683104)] [[Download](https://zenodo.org/records/12683104/files/images.zip?download=1)] | Candidate |
| 2023 | **CountBench** | general scene | 540 image-text examples | caption;object phrase;integer count | [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Paiss_Teaching_CLIP_to_Count_to_Ten_ICCV_2023_paper.html)] | Verified |
| 2023 | **FSC-147-D** | general scene | same 6,135 images as FSC-147 | natural-language target descriptions;original FSC-147 points/boxes/counts | [[Paper](https://arxiv.org/abs/2306.01851)] [[Project](https://www.robots.ox.ac.uk/~vgg/research/countx/)] [[Download](https://github.com/niki-amini-naieni/CounTX)] | Verified |
| 2023 | **IOCfish5K** | wildlife;underwater | 5,637 images;659,024 fish instances | point annotations;counts | [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Sun_Indiscernible_Object_Counting_in_Underwater_Scenes_CVPR_2023_paper.html)] | Verified |
| 2022 | **CoNIC** | histopathology | 4,981 image patches;about 432K nuclei | instance masks;centroids;class labels | [[Paper](https://arxiv.org/abs/2111.14485)] [[Project](https://conic-challenge.grand-challenge.org/)] | Verified |
| 2022 | **FSCD-147** | general scene | 6,135 images; exhaustive boxes added for validation and test | points;three exemplar boxes;target bounding boxes on validation/test;counts | [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800336.pdf)] [[Project](https://github.com/VinAIResearch/Counting-DETR)] | Verified |
| 2022 | **FSCD-LVIS** | general scene | 6,195 images;at least 220.7K instances | center points;exemplar boxes;target boxes | [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800336.pdf)] [[Project](https://github.com/VinAIResearch/Counting-DETR)] | Verified |
| 2021 | **AGAR** | microbiology | 18,000 images;about 336K colonies | boxes;class labels;counts | [[Paper](https://arxiv.org/abs/2108.01234)] | Verified |
| 2021 | **DroneCrowd** | crowd;drone | 112 clips;33,600 HD frames;4.8M head annotations;20,800 trajectories | head points;track identities;trajectories;video-level attributes | [[Paper](https://arxiv.org/abs/2105.02440)] | Verified |
| 2021 | **FSC-147** | general scene | 6,135 images;343,818 object instances | center points;3 exemplar boxes per image;counts | [[Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.html)] [[Project](https://github.com/cvlab-stonybrook/LearningToCountEverything)] | Verified |
| 2021 | **GWHD 2021** | agriculture | 6,515 images;about 275K wheat heads | axis-aligned boxes;domain/location metadata | [[Paper](https://doi.org/10.34133/2020/3521852)] [[Project](https://www.global-wheat.com/)] | Verified |
| 2021 | **LIVECell** | cellular microscopy | 5,239 images;over 1.6M cells | instance masks;polygons;boxes | [[Paper](https://doi.org/10.1038/s41592-021-01249-6)] [[Project](https://sartorius-research.github.io/LIVECell/)] | Verified |
| 2021 | **Lizard** | histopathology | 291 image regions;about 495K nuclei | instance masks;class labels;centroids | [[Paper](https://openaccess.thecvf.com/content/ICCV2021W/CDPath/papers/Graham_Lizard_A_Large-Scale_Dataset_for_Colonic_Nuclear_Instance_Segmentation_and_ICCVW_2021_paper.pdf)] [[Project](https://warwick.ac.uk/fac/cross_fac/tia/data/lizard/)] | Verified |
| 2021 | **NuCLS** | histopathology | 1,744 ROIs;over 220K nuclei | boxes;polygons;class labels;observer annotations | [[Paper](https://arxiv.org/abs/2102.09099)] [[Project](https://sites.google.com/view/nucls)] | Candidate |
| 2020 | **BCData** | histopathology | 1,338 images;about 181K cells | cell-center points;counts | [[Paper](https://doi.org/10.1007/978-3-030-59722-1_28)] [[Project](https://sites.google.com/view/bcdataset)] | Verified |
| 2020 | **JHU-CROWD++** | crowd | 4,372 images;about 1.51M annotations | head points;approximate boxes;occlusion;blur;weather and illumination attributes | [[Paper](https://arxiv.org/abs/2004.03597)] [[Project](https://github.com/svishwa/crowd-counting)] | Verified |
| 2020 | **MoNuSAC** | histopathology | 209 images from 46 patients | instance masks;class labels | [[Paper](https://doi.org/10.1109/TMI.2021.3085712)] [[Project](https://monusac-2020.grand-challenge.org/Data/)] | Verified |
| 2020 | **NWPU-Crowd** | crowd | 5,109 images;2,133,375 heads | head points;head boxes;negative images | [[Paper](https://arxiv.org/abs/2001.03360)] [[Project](https://gjy3035.github.io/NWPU-Crowd-Sample-Code/)] | Verified |
| 2019 | **FDST** | crowd | 15,000 frames;394,081 head annotations | head points;frame counts | [[Paper](https://arxiv.org/abs/1907.02749)] [[Project](https://github.com/sweetyy83/Lstn_fdst_dataset)] | Verified |
| 2019 | **GCC** | crowd | 15,212 images;7,625,843 people | head points;density/count metadata;scene and camera attributes | [[Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Learning_From_Synthetic_Data_for_Crowd_Counting_in_the_Wild_CVPR_2019_paper.html)] [[Project](https://gjy3035.github.io/GCC-CL/)] | Verified |
| 2019 | **SKU-110K** | retail;industrial-adjacent | 11,762 images;about 1.73M object instances | axis-aligned boxes;counts derivable | [[Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Goldman_Precise_Detection_in_Densely_Packed_Scenes_CVPR_2019_paper.html)] [[Project](https://github.com/eg4000/SKU110K_CVPR19)] | Verified |
| 2019 | **TallyQA** | general scene | 165K source images;287,907 questions | question;integer answer;simple/complex flag;source IDs | [[Paper](https://arxiv.org/abs/1810.12440)] [[Project](https://www.manojacharya.com/tallyqa.html)] [[Download](https://github.com/manoja328/TallyQA_dataset)] | Verified |
| 2018 | **UCF-QNRF** | crowd | 1,535 images;1,251,642 person annotations | head points;image-level counts | [[Paper](https://arxiv.org/abs/1807.09697)] [[Project](https://www.crcv.ucf.edu/research/data-sets/ucf-qnrf/)] | Verified |
| 2017 | **CARPK** | vehicle;remote sensing | 1,448 images;89,777 cars | axis-aligned boxes;image-level counts | [[Paper](https://openaccess.thecvf.com/content_iccv_2017/html/Hsieh_Drone-Based_Object_Counting_ICCV_2017_paper.html)] [[Project](https://lafi.github.io/LPN/)] | Verified |
| 2017 | **MoNuSeg** | histopathology | 44 images | instance masks;centroids derivable | [[Paper](https://doi.org/10.1109/TMI.2017.2677499)] [[Project](https://monuseg.grand-challenge.org/Data/)] | Verified |
| 2017 | **MTC** | agriculture | 361 images | dot annotations;image-level counts | [[Paper](https://doi.org/10.1186/s13007-017-0224-0)] [[Project](https://github.com/poppinace/mtc)] | Verified |
| 2017 | **PUCPR+** | vehicle;surveillance | 125 images;instance total unknown | axis-aligned boxes;image-level counts | [[Paper](https://openaccess.thecvf.com/content_iccv_2017/html/Hsieh_Drone-Based_Object_Counting_ICCV_2017_paper.html)] [[Project](https://lafi.github.io/LPN/)] | Candidate |
| 2016 | **COWC** | vehicle;remote sensing | 53 large image scenes;32,716 annotated cars | axis-aligned boxes;counts | [[Paper](https://arxiv.org/abs/1609.04453)] [[Project](https://gdo152.llnl.gov/cowc/)] | Verified |
| 2016 | **Penguin Counting Dataset** | wildlife | 80,095 images;575,082 annotated penguins | crowd-sourced points;annotator uncertainty;counts | [[Paper](https://ora.ox.ac.uk/objects/uuid%3A9bb7cbd9-42fc-416a-9cca-dd07c25f9fb1)] [[Project](https://www.robots.ox.ac.uk/~vgg/research/counting/index.html)] | Verified |
| 2016 | **ShanghaiTech** | crowd | 1,198 images;330,165 annotated people | head-center points;image-level counts | [[Paper](https://openaccess.thecvf.com/content_cvpr_2016/html/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.html)] | Verified |
| 2015 | **CVPPP Leaf Counting Challenge** | agriculture | 1,311 images;about 18,016 leaf instances across commonly aggregated releases | leaf centers;instance masks;image-level counts | [[Paper](https://doi.org/10.5244/C.29.CVPPP.1)] [[Project](https://www.plant-phenotyping.org/datasets-home)] | Verified |
| 2015 | **TRANCOS** | vehicle;traffic | 1,244 images;46,796 vehicles | vehicle-center points;ROI masks;image-level counts | [[Paper](https://doi.org/10.1016/j.neucom.2015.02.101)] [[Project](https://gram.web.uah.es/data/datasets/trancos/index.html)] | Verified |
| 2015 | **WorldExpo'10** | crowd | 3,980 frames;225,216 person annotations | head points;ROI masks;perspective maps | [[Paper](https://openaccess.thecvf.com/content_cvpr_2015/html/Zhang_Cross-Scene_Crowd_Counting_2015_CVPR_paper.html)] | Verified |
| 2013 | **UCF_CC_50** | crowd | 50 images;63,974 person annotations | head points;image-level counts | [[Paper](https://openaccess.thecvf.com/content_cvpr_2013/html/Idrees_Multi-source_Multi-scale_Counting_2013_CVPR_paper.html)] | Verified |
| 2010 | **VGG Synthetic Cells** | cellular microscopy | 200 images | cell-center points;counts | [[Paper](https://proceedings.neurips.cc/paper/2010/hash/fe73f687e5bc5280214e0486b273a5f9-Abstract.html)] [[Project](https://robots.ox.ac.uk/~vgg/research/counting/index.html)] | Verified |

</details>

## Papers

### Open-vocabulary Counting

*36 papers.*

#### 2026

- **[AdaCount]** AdaCount: Training-Free Similarity-Guided Spatial and Feature Adaptation for Zero-Shot Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2607.02139)]
- **[QICA]** Boosting Quantitive and Spatial Awareness for Zero-Shot Object Counting. (**CVPR 2026**) [[Paper](https://arxiv.org/abs/2603.16129)]
- **[Count Anything]** Count Anything. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.30846)] [[Code](https://github.com/Mengqi-Lei/count-anything)]
- **[HieraCount]** Count Anything at Any Granularity. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.10887)] [[Code](https://verg-avesta.github.io/KubriCount/)]
- **[CountGD++]** CountGD++: Generalized Prompting for Open-World Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Amini-Naieni_CountGD_Generalized_Prompting_for_Open-World_Counting_CVPR_2026_paper.html)] [[Code](https://github.com/niki-amini-naieni/CountGDPlusPlus)]
- **[PrACo++]** Does It Really Count? Assessing Semantic Grounding in Text-Guided Class-Agnostic Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.02752)]
- **[MambaCount]** MambaCount: Efficient Text-Guided Open-Vocabulary Object Counting with Spatial Sparse State Space Duality Block. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17650)]
- **[CountVid]** Open-World Object Counting in Videos. (**AAAI 2026**) [[Paper](https://arxiv.org/abs/2506.15368)] [[Code](https://github.com/niki-amini-naieni/CountVid)]
- **[RS-OVC]** RS-OVC: Open-Vocabulary Counting for Remote-Sensing Data. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2604.08704)]
- **[RT-Counter]** RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17561)] [[Code](https://github.com/Jason-Mar1/RT-Counter)]
- **[Dual-TTT]** Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17601)]
- **[MixCount]** The MixCount Dataset: Bridging the Data Gap for Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.18063)] [[Code](https://corentindumery.github.io/projects/mixcount.html)]

#### 2025

- **[PairTally]** Can Current AI Models Count What We Mean, Not What They See? A Benchmark and Systematic Evaluation. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2509.13939)]
- **[CountOCC]** Counting Through Occlusion: Framework for Open World Amodal Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2511.12702)]
- **[CountSE]** CountSE: Soft Exemplar Open-Set Object Counting. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_CountSE_Soft_Exemplar_Open-set_Object_Counting_ICCV_2025_paper.html)] [[Code](https://github.com/pppppz22/CountSE)]
- **[CountZES]** CountZES: Counting via Zero-Shot Exemplar Selection. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2512.16415)]
- **[LGCount]** Enhancing Zero-Shot Object Counting via Text-Guided Local Ranking and Number-Evoked Global Attention. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Enhancing_Zero-shot_Object_Counting_via_Text-guided_Local_Ranking_and_Number-evoked_ICCV_2025_paper.html)] [[Code](https://github.com/zaqai/LGCount)]
- **[RichCount]** Expanding Zero-Shot Object Counting with Rich Prompts. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2505.15398)]
- **[FocalCount]** FocalCount: Towards Class-Count Imbalance in Class-Agnostic Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2502.10677)]
- **[PrACo]** Mind the Prompt: A Novel Benchmark for Prompt-Based Class-Agnostic Counting. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Ciampi_Mind_the_Prompt_A_Novel_Benchmark_for_Prompt-Based_Class-Agnostic_Counting_WACV_2025_paper.html)] [[Code](https://github.com/ciampluca/PrACo)]
- **[SDVPT]** SDVPT: Semantic-Driven Visual Prompt Tuning for Open-World Object Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2504.17395)]
- **[T2ICount]** T2ICount: Enhancing Cross-Modal Understanding for Zero-Shot Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_T2ICount_Enhancing_Cross-modal_Understanding_for_Zero-Shot_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/cha15yq/T2ICount)]
- **[QUANet]** Text-Promptable Object Counting via Quantity Awareness Enhancement. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2507.06679)] [[Code](https://github.com/viscom-tongji/QUANet)]
- **[TrueCount]** TrueCount: Improving Open-World Object Counting with Visual-Language Models and Dynamic Multi-Modal Inputs. (**ACM MM 2025**) [[Paper](https://doi.org/10.1145/3746027.3755426)]
- **[VQCounter]** VQCounter: Designing Visual Prompt Queue for Accurate Open-World Counting. (**IJCAI 2025**) [[Paper](https://www.ijcai.org/proceedings/2025/252)]
- **[YOLO-Count]** YOLO-Count: Differentiable Object Counting for Text-to-Image Generation. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zeng_YOLO-Count_Differentiable_Object_Counting_for_Text-to-Image_Generation_ICCV_2025_paper.html)]

#### 2024

- **[CountDiff]** Class-Agnostic Object Counting with Text-to-Image Diffusion Model. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8663_ECCV_2024_paper.php)]
- **[CountGD]** CountGD: Multi-Modal Open-World Counting. (**NeurIPS 2024**) [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html)] [[Code](https://github.com/niki-amini-naieni/CountGD)]
- **[DAVE]** DAVE: A Detect-and-Verify Paradigm for Low-Shot Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/jerpelhan/DAVE)]
- **[PseCo]** Point Segment and Count: A Generalized Framework for Object Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Point_Segment_and_Count_A_Generalized_Framework_for_Object_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/Hzzone/PseCo)]
- **[GroundingREC]** Referring Expression Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Dai_Referring_Expression_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/sydai/referring-expression-counting)]
- **[VLCounter]** VLCounter: Text-Aware Visual Representation for Zero-Shot Object Counting. (**AAAI 2024**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28050)] [[Code](https://github.com/Seunggu0305/VLCounter)]
- **[VA-Count]** Zero-Shot Object Counting with Good Exemplars. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00812.pdf)]

#### 2023

- **[CLIP-Count]** CLIP-Count: Towards Text-Guided Zero-Shot Object Counting. (**ACM MM 2023**) [[Paper](https://arxiv.org/abs/2305.07304)] [[Code](https://github.com/songrise/CLIP-Count)]
- **[CounTX]** Open-World Text-Specified Object Counting. (**BMVC 2023**) [[Paper](https://arxiv.org/abs/2306.01851)] [[Code](https://www.robots.ox.ac.uk/~vgg/research/countx/)]
- **[ZSC]** Zero-Shot Object Counting. (**CVPR 2023**) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Zero-Shot_Object_Counting_CVPR_2023_paper.html)] [[Code](https://github.com/cvlab-stonybrook/zero-shot-counting)]

### Exemplar-based Counting

*37 papers.*

#### 2026

- **[HieraCount]** Count Anything at Any Granularity. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.10887)] [[Code](https://verg-avesta.github.io/KubriCount/)]
- **[CountGD++]** CountGD++: Generalized Prompting for Open-World Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Amini-Naieni_CountGD_Generalized_Prompting_for_Open-World_Counting_CVPR_2026_paper.html)] [[Code](https://github.com/niki-amini-naieni/CountGDPlusPlus)]
- **[CountingDINO]** CountingDINO: A Training-Free Pipeline for Class-Agnostic Counting using Unsupervised Backbones. (**WACV 2026**) [[Paper](https://openaccess.thecvf.com/content/WACV2026/html/Pacini_CountingDINO_A_Training-free_Pipeline_for_Class-Agnostic_Counting_using_Unsupervised_Backbones_WACV_2026_paper.html)]
- **[GeCo2]** Generalized-Scale Object Counting with Gradual Query Aggregation. (**AAAI 2026**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37780)] [[Code](https://github.com/jerpelhan/GECO2/)]
- **[CountVid]** Open-World Object Counting in Videos. (**AAAI 2026**) [[Paper](https://arxiv.org/abs/2506.15368)] [[Code](https://github.com/niki-amini-naieni/CountVid)]

#### 2025

- **[TFCAC]** A Simple-but-Effective Baseline for Training-Free Class-Agnostic Counting. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Lin_A_Simple-but-Effective_Baseline_for_Training-Free_Class-Agnostic_Counting_WACV_2025_paper.html)]
- **[PairTally]** Can Current AI Models Count What We Mean, Not What They See? A Benchmark and Systematic Evaluation. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2509.13939)]
- **[CountOCC]** Counting Through Occlusion: Framework for Open World Amodal Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2511.12702)]
- **[CACAL]** Counting with Ease: Class-Agnostic Counting via One-Shot Detection across Diverse Domains. (**Neural Networks 2025**) [[Paper](https://www.sciencedirect.com/science/article/pii/S0893608025008421)] [[Code](https://github.com/imMid-Star/CACAL)]
- **[FocalCount]** FocalCount: Towards Class-Count Imbalance in Class-Agnostic Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2502.10677)]
- **[PLS-Count]** Learning to Count from Pseudo-Labeled Segmentation. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/papers/Xu_Learning_to_Count_from_Pseudo-Labeled_Segmentation_WACV_2025_paper.pdf)]
- **[PrACo]** Mind the Prompt: A Novel Benchmark for Prompt-Based Class-Agnostic Counting. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Ciampi_Mind_the_Prompt_A_Novel_Benchmark_for_Prompt-Based_Class-Agnostic_Counting_WACV_2025_paper.html)] [[Code](https://github.com/ciampluca/PrACo)]
- **[SDVPT]** SDVPT: Semantic-Driven Visual Prompt Tuning for Open-World Object Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2504.17395)]
- **[URM]** Single Domain Generalization for Few-Shot Counting via Universal Representation Matching. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Single_Domain_Generalization_for_Few-Shot_Counting_via_Universal_Representation_Matching_CVPR_2025_paper.html)] [[Code](https://github.com/jbr97/URM)]
- **[VQCounter]** VQCounter: Designing Visual Prompt Queue for Accurate Open-World Counting. (**IJCAI 2025**) [[Paper](https://www.ijcai.org/proceedings/2025/252)]

#### 2024

- **[UPC]** A Fixed-Point Approach to Unified Prompt-Based Counting. (**AAAI 2024**) [[Paper](https://arxiv.org/abs/2403.10236)]
- **[GeCo]** A Novel Unified Architecture for Low-Shot Counting by Detection and Segmentation. (**NeurIPS 2024**) [[Paper](https://arxiv.org/abs/2409.18686)] [[Code](https://github.com/jerpelhan/GeCo)]
- **[MGCAC]** A Recipe for CAC: Mosaic-Based Generalized Loss for Improved Class-Agnostic Counting. (**ACCV 2024**) [[Paper](https://openaccess.thecvf.com/content/ACCV2024/html/Chou_A_Recipe_for_CAC_Mosaic-based_Generalized_Loss_for_Improved_Class-Agnostic_ACCV_2024_paper.html)] [[Code](https://github.com/littlepenguin89106/MGCAC)]
- **[CountDiff]** Class-Agnostic Object Counting with Text-to-Image Diffusion Model. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8663_ECCV_2024_paper.php)]
- **[CountGD]** CountGD: Multi-Modal Open-World Counting. (**NeurIPS 2024**) [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html)] [[Code](https://github.com/niki-amini-naieni/CountGD)]
- **[DAVE]** DAVE: A Detect-and-Verify Paradigm for Low-Shot Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/jerpelhan/DAVE)]
- **[PseCo]** Point Segment and Count: A Generalized Framework for Object Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Point_Segment_and_Count_A_Generalized_Framework_for_Object_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/Hzzone/PseCo)]
- **[SATCount]** SATCount: A Scale-Aware Transformer-Based Class-Agnostic Counting Framework. (**Neural Networks 2024**) [[Paper](https://www.sciencedirect.com/science/article/pii/S089360802400042X)]
- **[TFCounter]** TFCounter: Polishing Gems for Training-Free Object Counting. (**arXiv 2024**) [[Paper](https://arxiv.org/abs/2405.02301)]
- **[TFPOC]** Training-Free Object Counting with Prompts. (**WACV 2024**) [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Shi_Training-Free_Object_Counting_With_Prompts_WACV_2024_paper.html)] [[Code](https://github.com/shizenglin/training-free-object-counter)]
- **[CACViT]** Vision Transformer Off-the-Shelf: A Surprising Baseline for Few-Shot Class-Agnostic Counting. (**AAAI 2024**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28396)]

#### 2023

- **[LOCA]** A Low-Shot Object Counting Network with Iterative Prototype Adaptation. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Dukic_A_Low-Shot_Object_Counting_Network_With_Iterative_Prototype_Adaptation_ICCV_2023_paper.html)] [[Code](https://github.com/djukicn/loca)]
- **[ConCoNet]** ConCoNet: Class-Agnostic Counting with Positive and Negative Exemplars. (**Pattern Recognition Letters 2023**) [[Paper](https://doi.org/10.1016/j.patrec.2023.04.018)]
- **[SAFECount]** Few-Shot Object Counting with Similarity-Aware Feature Enhancement. (**WACV 2023**) [[Paper](https://openaccess.thecvf.com/content/WACV2023/html/You_Few-Shot_Object_Counting_With_Similarity-Aware_Feature_Enhancement_WACV_2023_paper.html)] [[Code](https://github.com/zhiyuanyou/SAFECount)]
- **[ICACount]** Interactive Class-Agnostic Object Counting. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_Interactive_Class-Agnostic_Object_Counting_ICCV_2023_paper.html)] [[Code](https://yifehuang97.github.io/ICACountProjectPage/)]
- **[MACnet]** MACnet: Mask Augmented Counting Network for Class-Agnostic Counting. (**Pattern Recognition Letters 2023**) [[Paper](https://www.sciencedirect.com/science/article/pii/S016786552300082X)]

#### 2022

- **[RCAC]** Class-Agnostic Object Counting Robust to Intraclass Diversity. (**ECCV 2022**) [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/642_ECCV_2022_paper.php)] [[Code](https://github.com/Yankeegsj/RCAC)]
- **[CounTR]** CounTR: Transformer-Based Generalised Visual Counting. (**BMVC 2022**) [[Paper](https://ora.ox.ac.uk/objects/uuid%3Aebe0f751-f83d-4b71-8fc4-4298cb0cb658)] [[Code](https://github.com/Verg-Avesta/CounTR)]
- **[Counting-DETR]** Few-Shot Object Counting and Detection. (**ECCV 2022**) [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800336.pdf)] [[Code](https://github.com/VinAIResearch/Counting-DETR)]
- **[BMNet+]** Represent Compare and Learn: A Similarity-Aware Framework for Class-Agnostic Counting. (**CVPR 2022**) [[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shi_Represent_Compare_and_Learn_A_Similarity-Aware_Framework_for_Class-Agnostic_Counting_CVPR_2022_paper.html)] [[Code](https://tiny.one/BMNet)]

#### 2021

- **[FamNet]** Learning To Count Everything. (**CVPR 2021**) [[Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.html)] [[Code](https://github.com/cvlab-stonybrook/LearningToCountEverything)]

#### 2018

- **[GMN]** Class-Agnostic Counting. (**ACCV 2018**) [[Paper](https://ora.ox.ac.uk/objects/uuid%3A0700b0af-1b14-4f4e-a7bc-8f38e93b4a51)]

### MLLM-based Counting

*18 papers.*

#### 2026

- **[WS-COC]** Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting. (**ICLR 2026**) [[Paper](https://arxiv.org/abs/2602.12774)] [[Code](https://github.com/viscom-tongji/WS-COC)]
- **[CountGD++]** CountGD++: Generalized Prompting for Open-World Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Amini-Naieni_CountGD_Generalized_Prompting_for_Open-World_Counting_CVPR_2026_paper.html)] [[Code](https://github.com/niki-amini-naieni/CountGDPlusPlus)]
- **[EC-Bench]** EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2603.29943)]
- **[HoloCount]** HoloCount: A Holistic Visual Counting Benchmark for MLLMs. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2607.06420)] [[Code](https://github.com/MM-MVR/HoloCount)]
- **[SVCBench]** SVCBench: A Streaming Video Counting Benchmark for Spatial-Temporal State Maintenance. (**ECCV 2026**) [[Paper](https://arxiv.org/abs/2603.12703)] [[Code](https://buaa-colalab.github.io/SVCBench/)]
- **[CountScope]** Understanding Counting Mechanisms in Large Language and Vision-Language Models. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hasani_Understanding_Counting_Mechanisms_in_Large_Language_and_Vision-Language_Models_CVPR_2026_paper.html)] [[Code](https://github.com/sharif-ml-lab/counting-mechanisms)]
- **[UNICBench]** UNICBench: UNIfied Counting Benchmark for MLLM. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rong_UNICBench_UNIfied_Counting_Benchmark_for_MLLM_CVPR_2026_paper.html)]

#### 2025

- **[AV-Reasoner]** AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2506.05328)] [[Code](https://github.com/AV-Reasoner/AV-Reasoner)]
- **[PairTally]** Can Current AI Models Count What We Mean, Not What They See? A Benchmark and Systematic Evaluation. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2509.13939)]
- **[CAPTURe]** CAPTURe: Evaluating Spatial Reasoning in Vision Language Models via Occluded Object Counting. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Pothiraj_CAPTURE_Evaluating_Spatial_Reasoning_in_Vision_Language_Models_via_Occluded_ICCV_2025_paper.html)] [[Code](https://github.com/atinpothiraj/CAPTURe)]
- **[CountQA]** CountQA: How Well Do MLLMs Count in the Wild? (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2508.06585)]
- **[T2ICount]** T2ICount: Enhancing Cross-Modal Understanding for Zero-Shot Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_T2ICount_Enhancing_Cross-modal_Understanding_for_Zero-Shot_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/cha15yq/T2ICount)]
- **[TrueCount]** TrueCount: Improving Open-World Object Counting with Visual-Language Models and Dynamic Multi-Modal Inputs. (**ACM MM 2025**) [[Paper](https://doi.org/10.1145/3746027.3755426)]

#### 2024

- **[CountGD]** CountGD: Multi-Modal Open-World Counting. (**NeurIPS 2024**) [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html)] [[Code](https://github.com/niki-amini-naieni/CountGD)]
- **[VLCounter]** VLCounter: Text-Aware Visual Representation for Zero-Shot Object Counting. (**AAAI 2024**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28050)] [[Code](https://github.com/Seunggu0305/VLCounter)]

#### 2023

- **[CLIP-Count]** CLIP-Count: Towards Text-Guided Zero-Shot Object Counting. (**ACM MM 2023**) [[Paper](https://arxiv.org/abs/2305.07304)] [[Code](https://github.com/songrise/CLIP-Count)]
- **[CrowdCLIP]** CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model. (**CVPR 2023**) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Liang_CrowdCLIP_Unsupervised_Crowd_Counting_via_Vision-Language_Model_CVPR_2023_paper.html)] [[Code](https://github.com/dk-liang/CrowdCLIP)]
- **[CountBench]** Teaching CLIP to Count to Ten. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Paiss_Teaching_CLIP_to_Count_to_Ten_ICCV_2023_paper.html)]

### Class-agnostic Counting

*66 papers.*

#### 2026

- **[AdaCount]** AdaCount: Training-Free Similarity-Guided Spatial and Feature Adaptation for Zero-Shot Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2607.02139)]
- **[QICA]** Boosting Quantitive and Spatial Awareness for Zero-Shot Object Counting. (**CVPR 2026**) [[Paper](https://arxiv.org/abs/2603.16129)]
- **[WS-COC]** Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting. (**ICLR 2026**) [[Paper](https://arxiv.org/abs/2602.12774)] [[Code](https://github.com/viscom-tongji/WS-COC)]
- **[Count Anything]** Count Anything. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.30846)] [[Code](https://github.com/Mengqi-Lei/count-anything)]
- **[HieraCount]** Count Anything at Any Granularity. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.10887)] [[Code](https://verg-avesta.github.io/KubriCount/)]
- **[CountGD++]** CountGD++: Generalized Prompting for Open-World Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Amini-Naieni_CountGD_Generalized_Prompting_for_Open-World_Counting_CVPR_2026_paper.html)] [[Code](https://github.com/niki-amini-naieni/CountGDPlusPlus)]
- **[CountingDINO]** CountingDINO: A Training-Free Pipeline for Class-Agnostic Counting using Unsupervised Backbones. (**WACV 2026**) [[Paper](https://openaccess.thecvf.com/content/WACV2026/html/Pacini_CountingDINO_A_Training-free_Pipeline_for_Class-Agnostic_Counting_using_Unsupervised_Backbones_WACV_2026_paper.html)]
- **[PrACo++]** Does It Really Count? Assessing Semantic Grounding in Text-Guided Class-Agnostic Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.02752)]
- **[GeCo2]** Generalized-Scale Object Counting with Gradual Query Aggregation. (**AAAI 2026**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37780)] [[Code](https://github.com/jerpelhan/GECO2/)]
- **[MambaCount]** MambaCount: Efficient Text-Guided Open-Vocabulary Object Counting with Spatial Sparse State Space Duality Block. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17650)]
- **[OCCAM]** OCCAM: Class-Agnostic Training-Free Prior-Free and Multi-Class Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2601.13871)] [[Code](https://mikespanak.github.io/OCCAM_counter/)]
- **[CountVid]** Open-World Object Counting in Videos. (**AAAI 2026**) [[Paper](https://arxiv.org/abs/2506.15368)] [[Code](https://github.com/niki-amini-naieni/CountVid)]
- **[TPC-268]** Plant Taxonomy Meets Plant Counting: A Fine-Grained Taxonomic Dataset for Counting Hundreds of Plant Species. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Plant_Taxonomy_Meets_Plant_Counting_A_Fine-Grained_Taxonomic_Dataset_for_CVPR_2026_paper.html)] [[Code](https://github.com/tiny-smart/TPC-268)]
- **[RT-Counter]** RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17561)] [[Code](https://github.com/Jason-Mar1/RT-Counter)]
- **[UpCount]** Spatially-Aware Class-Agnostic Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2607.16826)] [[Code](https://github.com/r28112072-rgb/upcount)]
- **[Dual-TTT]** Test-Time Training for Robust Text-Guided Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2606.17601)]
- **[MixCount]** The MixCount Dataset: Bridging the Data Gap for Open-Vocabulary Object Counting. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2605.18063)] [[Code](https://corentindumery.github.io/projects/mixcount.html)]

#### 2025

- **[TFCAC]** A Simple-but-Effective Baseline for Training-Free Class-Agnostic Counting. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Lin_A_Simple-but-Effective_Baseline_for_Training-Free_Class-Agnostic_Counting_WACV_2025_paper.html)]
- **[PairTally]** Can Current AI Models Count What We Mean, Not What They See? A Benchmark and Systematic Evaluation. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2509.13939)]
- **[CountOCC]** Counting Through Occlusion: Framework for Open World Amodal Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2511.12702)]
- **[CACAL]** Counting with Ease: Class-Agnostic Counting via One-Shot Detection across Diverse Domains. (**Neural Networks 2025**) [[Paper](https://www.sciencedirect.com/science/article/pii/S0893608025008421)] [[Code](https://github.com/imMid-Star/CACAL)]
- **[CountSE]** CountSE: Soft Exemplar Open-Set Object Counting. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_CountSE_Soft_Exemplar_Open-set_Object_Counting_ICCV_2025_paper.html)] [[Code](https://github.com/pppppz22/CountSE)]
- **[CountZES]** CountZES: Counting via Zero-Shot Exemplar Selection. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2512.16415)]
- **[LGCount]** Enhancing Zero-Shot Object Counting via Text-Guided Local Ranking and Number-Evoked Global Attention. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Enhancing_Zero-shot_Object_Counting_via_Text-guided_Local_Ranking_and_Number-evoked_ICCV_2025_paper.html)] [[Code](https://github.com/zaqai/LGCount)]
- **[RichCount]** Expanding Zero-Shot Object Counting with Rich Prompts. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2505.15398)]
- **[FiGO]** FiGO: Fine-Grained Object Counting without Annotations. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2504.11705)]
- **[FocalCount]** FocalCount: Towards Class-Count Imbalance in Class-Agnostic Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2502.10677)]
- **[PLS-Count]** Learning to Count from Pseudo-Labeled Segmentation. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/papers/Xu_Learning_to_Count_from_Pseudo-Labeled_Segmentation_WACV_2025_paper.pdf)]
- **[PrACo]** Mind the Prompt: A Novel Benchmark for Prompt-Based Class-Agnostic Counting. (**WACV 2025**) [[Paper](https://openaccess.thecvf.com/content/WACV2025/html/Ciampi_Mind_the_Prompt_A_Novel_Benchmark_for_Prompt-Based_Class-Agnostic_Counting_WACV_2025_paper.html)] [[Code](https://github.com/ciampluca/PrACo)]
- **[SDVPT]** SDVPT: Semantic-Driven Visual Prompt Tuning for Open-World Object Counting. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2504.17395)]
- **[URM]** Single Domain Generalization for Few-Shot Counting via Universal Representation Matching. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Single_Domain_Generalization_for_Few-Shot_Counting_via_Universal_Representation_Matching_CVPR_2025_paper.html)] [[Code](https://github.com/jbr97/URM)]
- **[T2ICount]** T2ICount: Enhancing Cross-Modal Understanding for Zero-Shot Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Qian_T2ICount_Enhancing_Cross-modal_Understanding_for_Zero-Shot_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/cha15yq/T2ICount)]
- **[QUANet]** Text-Promptable Object Counting via Quantity Awareness Enhancement. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2507.06679)] [[Code](https://github.com/viscom-tongji/QUANet)]
- **[TrueCount]** TrueCount: Improving Open-World Object Counting with Visual-Language Models and Dynamic Multi-Modal Inputs. (**ACM MM 2025**) [[Paper](https://doi.org/10.1145/3746027.3755426)]
- **[VQCounter]** VQCounter: Designing Visual Prompt Queue for Accurate Open-World Counting. (**IJCAI 2025**) [[Paper](https://www.ijcai.org/proceedings/2025/252)]

#### 2024

- **[UPC]** A Fixed-Point Approach to Unified Prompt-Based Counting. (**AAAI 2024**) [[Paper](https://arxiv.org/abs/2403.10236)]
- **[GeCo]** A Novel Unified Architecture for Low-Shot Counting by Detection and Segmentation. (**NeurIPS 2024**) [[Paper](https://arxiv.org/abs/2409.18686)] [[Code](https://github.com/jerpelhan/GeCo)]
- **[MGCAC]** A Recipe for CAC: Mosaic-Based Generalized Loss for Improved Class-Agnostic Counting. (**ACCV 2024**) [[Paper](https://openaccess.thecvf.com/content/ACCV2024/html/Chou_A_Recipe_for_CAC_Mosaic-based_Generalized_Loss_for_Improved_Class-Agnostic_ACCV_2024_paper.html)] [[Code](https://github.com/littlepenguin89106/MGCAC)]
- **[ABC123]** ABC Easy as 123: A Blind Counter for Exemplar-Free Multi-Class Class-Agnostic Counting. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01761.pdf)]
- **[CountDiff]** Class-Agnostic Object Counting with Text-to-Image Diffusion Model. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8663_ECCV_2024_paper.php)]
- **[CountGD]** CountGD: Multi-Modal Open-World Counting. (**NeurIPS 2024**) [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/57c56985d9afe89bf78a8264c91071aa-Abstract-Conference.html)] [[Code](https://github.com/niki-amini-naieni/CountGD)]
- **[DAVE]** DAVE: A Detect-and-Verify Paradigm for Low-Shot Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/jerpelhan/DAVE)]
- **[SelfCollages]** Learning to Count without Annotations. (**CVPR 2024**) [[Paper](https://doi.org/10.1109/CVPR52733.2024.02163)] [[Code](https://github.com/lukasknobel/SelfCollages)]
- **[PseCo]** Point Segment and Count: A Generalized Framework for Object Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Point_Segment_and_Count_A_Generalized_Framework_for_Object_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/Hzzone/PseCo)]
- **[GroundingREC]** Referring Expression Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Dai_Referring_Expression_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/sydai/referring-expression-counting)]
- **[SATCount]** SATCount: A Scale-Aware Transformer-Based Class-Agnostic Counting Framework. (**Neural Networks 2024**) [[Paper](https://www.sciencedirect.com/science/article/pii/S089360802400042X)]
- **[TFCounter]** TFCounter: Polishing Gems for Training-Free Object Counting. (**arXiv 2024**) [[Paper](https://arxiv.org/abs/2405.02301)]
- **[TFPOC]** Training-Free Object Counting with Prompts. (**WACV 2024**) [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Shi_Training-Free_Object_Counting_With_Prompts_WACV_2024_paper.html)] [[Code](https://github.com/shizenglin/training-free-object-counter)]
- **[CACViT]** Vision Transformer Off-the-Shelf: A Surprising Baseline for Few-Shot Class-Agnostic Counting. (**AAAI 2024**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28396)]
- **[VLCounter]** VLCounter: Text-Aware Visual Representation for Zero-Shot Object Counting. (**AAAI 2024**) [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/28050)] [[Code](https://github.com/Seunggu0305/VLCounter)]
- **[VA-Count]** Zero-Shot Object Counting with Good Exemplars. (**ECCV 2024**) [[Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00812.pdf)]

#### 2023

- **[LOCA]** A Low-Shot Object Counting Network with Iterative Prototype Adaptation. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Dukic_A_Low-Shot_Object_Counting_Network_With_Iterative_Prototype_Adaptation_ICCV_2023_paper.html)] [[Code](https://github.com/djukicn/loca)]
- **[CLIP-Count]** CLIP-Count: Towards Text-Guided Zero-Shot Object Counting. (**ACM MM 2023**) [[Paper](https://arxiv.org/abs/2305.07304)] [[Code](https://github.com/songrise/CLIP-Count)]
- **[ConCoNet]** ConCoNet: Class-Agnostic Counting with Positive and Negative Exemplars. (**Pattern Recognition Letters 2023**) [[Paper](https://doi.org/10.1016/j.patrec.2023.04.018)]
- **[SAFECount]** Few-Shot Object Counting with Similarity-Aware Feature Enhancement. (**WACV 2023**) [[Paper](https://openaccess.thecvf.com/content/WACV2023/html/You_Few-Shot_Object_Counting_With_Similarity-Aware_Feature_Enhancement_WACV_2023_paper.html)] [[Code](https://github.com/zhiyuanyou/SAFECount)]
- **[ICACount]** Interactive Class-Agnostic Object Counting. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_Interactive_Class-Agnostic_Object_Counting_ICCV_2023_paper.html)] [[Code](https://yifehuang97.github.io/ICACountProjectPage/)]
- **[MACnet]** MACnet: Mask Augmented Counting Network for Class-Agnostic Counting. (**Pattern Recognition Letters 2023**) [[Paper](https://www.sciencedirect.com/science/article/pii/S016786552300082X)]
- **[CounTX]** Open-World Text-Specified Object Counting. (**BMVC 2023**) [[Paper](https://arxiv.org/abs/2306.01851)] [[Code](https://www.robots.ox.ac.uk/~vgg/research/countx/)]
- **[ZSC]** Zero-Shot Object Counting. (**CVPR 2023**) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Zero-Shot_Object_Counting_CVPR_2023_paper.html)] [[Code](https://github.com/cvlab-stonybrook/zero-shot-counting)]

#### 2022

- **[RCAC]** Class-Agnostic Object Counting Robust to Intraclass Diversity. (**ECCV 2022**) [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/642_ECCV_2022_paper.php)] [[Code](https://github.com/Yankeegsj/RCAC)]
- **[CounTR]** CounTR: Transformer-Based Generalised Visual Counting. (**BMVC 2022**) [[Paper](https://ora.ox.ac.uk/objects/uuid%3Aebe0f751-f83d-4b71-8fc4-4298cb0cb658)] [[Code](https://github.com/Verg-Avesta/CounTR)]
- **[RepRPN-Counter]** Exemplar Free Class Agnostic Counting. (**ACCV 2022**) [[Paper](https://openaccess.thecvf.com/content/ACCV2022/html/Ranjan_Exemplar_Free_Class_Agnostic_Counting_ACCV_2022_paper.html)] [[Code](https://github.com/Viresh-R/ExemplarFreeCounting)]
- **[Counting-DETR]** Few-Shot Object Counting and Detection. (**ECCV 2022**) [[Paper](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136800336.pdf)] [[Code](https://github.com/VinAIResearch/Counting-DETR)]
- **[BMNet+]** Represent Compare and Learn: A Similarity-Aware Framework for Class-Agnostic Counting. (**CVPR 2022**) [[Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Shi_Represent_Compare_and_Learn_A_Similarity-Aware_Framework_for_Class-Agnostic_Counting_CVPR_2022_paper.html)] [[Code](https://tiny.one/BMNet)]

#### 2021

- **[FamNet]** Learning To Count Everything. (**CVPR 2021**) [[Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.html)] [[Code](https://github.com/cvlab-stonybrook/LearningToCountEverything)]

#### 2018

- **[GMN]** Class-Agnostic Counting. (**ACCV 2018**) [[Paper](https://ora.ox.ac.uk/objects/uuid%3A0700b0af-1b14-4f4e-a7bc-8f38e93b4a51)]

### Class-specific Counting

*45 papers.*

#### 2027

- **[PRoFENCH]** PRoFENCH: A systematic study of multimodal fusion and generalization in WiFi–Vision wireless sensing for people counting. (**Ad Hoc Networks 2027**) [[Paper](https://doi.org/10.1016/j.adhoc.2026.104388)]
- **[Shang et al.]** Untangling context: A Gaussian Splatting-mediated Bayesian framework for crowd counting. (**Pattern Recognition 2027**) [[Paper](https://doi.org/10.1016/j.patcog.2026.114725)]

#### 2026

- **[Shu et al.]** Adapting Lightweight Image-Based Counting Models for Video Crowd Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_Adapting_Lightweight_Image-based_Counting_Models_for_Video_Crowd_Counting_CVPR_2026_paper.html)]
- **[Tripathi et al.]** Counting of rice panicles using drone mounted RGB sensor and deep learning approaches. (**Journal of Crop Science and Biotechnology 2026**) [[Paper](https://doi.org/10.1007/s12892-026-00377-9)]
- **[DG-Det]** Depth-Guided Video Object Counting in Crowded Scenes. (**ACM MM 2026**) [[Paper](https://arxiv.org/abs/2608.06236)] [[Code](https://github.com/streamer-AP/DG-Net)]
- **[StructGuide-YOLO]** Edge-guided structural conditioning for Gong-Che symbol localization and page-level counting in aged documents. (**Measurement Science and Technology 2026**) [[Paper](https://doi.org/10.1088/1361-6501/ae9f7c)]
- **[KBTrack]** KBTrack: cloud-enabled temporal identity inference for accurate counting in ornamental plant inventory management. (**Computers and Electronics in Agriculture 2026**) [[Paper](https://doi.org/10.1016/j.compag.2026.112307)]
- **[Zhou & Zhang]** Label-Efficient Remote Sensing Object Counting via Cascaded Foundation Models and Global-Local Ranking. (**IEEE GRSL 2026**) [[Paper](https://doi.org/10.1109/LGRS.2026.3726140)]
- **[Chen et al. (2026)]** One-Shot Crowd Counting With Density Guidance For Scene Adaptation. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2602.07955)]
- **[TPC-268]** Plant Taxonomy Meets Plant Counting: A Fine-Grained Taxonomic Dataset for Counting Hundreds of Plant Species. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Plant_Taxonomy_Meets_Plant_Counting_A_Fine-Grained_Taxonomic_Dataset_for_CVPR_2026_paper.html)] [[Code](https://github.com/tiny-smart/TPC-268)]
- **[RS-OVC]** RS-OVC: Open-Vocabulary Counting for Remote-Sensing Data. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2604.08704)]
- **[SCRSNet]** SCRSNet: An Efficient Crowd Counting via Lightweight Spatial-Channel Reconstructive and Scale-Aware Network. (**Expert Systems 2026**) [[Paper](https://doi.org/10.1111/exsy.70409)]
- **[GROC]** See What We Cannot See: A Geo-Guided Reasoning Benchmark for Object Counting under Adverse Earth Observation Conditions. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_See_What_We_Cannot_See_A_Geo-guided_Reasoning_Benchmark_for_CVPR_2026_paper.html)]

#### 2025

- **[3DC]** Counting Stacked Objects. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Dumery_Counting_Stacked_Objects_ICCV_2025_paper.html)] [[Code](https://corentindumery.github.io/projects/stacks.html)]
- **[Free Lunch]** Free Lunch Enhancements for Multi-Modal Crowd Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Meng_Free_Lunch_Enhancements_for_Multi-modal_Crowd_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/HenryCilence/Free-Lunch-Multimodal-Counting)]
- **[P2R]** Point-to-Region Loss for Semi-Supervised Point-Based Crowd Counting. (**CVPR 2025**) [[Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_Point-to-Region_Loss_for_Semi-Supervised_Point-Based_Crowd_Counting_CVPR_2025_paper.html)] [[Code](https://github.com/Elin24/P2RLoss)]
- **[SDNet]** Video Individual Counting for Moving Drones. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Video_Individual_Counting_for_Moving_Drones_ICCV_2025_paper.html)] [[Code](https://github.com/fyw1999/MovingDroneCrowd)]

#### 2024

- **[CrowdDiff]** CrowdDiff: Multi-hypothesis Crowd Density Estimation using Diffusion Models. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ranasinghe_CrowdDiff_Multi-hypothesis_Crowd_Density_Estimation_using_Diffusion_Models_CVPR_2024_paper.html)] [[Code](https://dylran.github.io/crowddiff.github.io/)]
- **[CeDiRNet]** Dense Center-Direction Regression for Object Counting and Localization with Point Supervision. (**Pattern Recognition 2024**) [[Paper](https://arxiv.org/abs/2408.14457)] [[Code](https://github.com/vicoslab/CeDiRNet)]
- **[mPrompt]** Regressor-Segmenter Mutual Prompt Learning for Crowd Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_Regressor-Segmenter_Mutual_Prompt_Learning_for_Crowd_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/csguomy/mPrompt)]
- **[MPCount]** Single Domain Generalization for Crowd Counting. (**CVPR 2024**) [[Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Peng_Single_Domain_Generalization_for_Crowd_Counting_CVPR_2024_paper.html)] [[Code](https://github.com/Shimmer93/MPCount)]

#### 2023

- **[Crowd-Hat]** Boosting Detection in Crowd Analysis via Underutilized Output Features. (**CVPR 2023**) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Wu_Boosting_Detection_in_Crowd_Analysis_via_Underutilized_Output_Features_CVPR_2023_paper.html)] [[Code](https://github.com/wskingdom/Crowd-Hat)]
- **[AWCC-Net]** Counting Crowds in Bad Weather. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_Counting_Crowds_in_Bad_Weather_ICCV_2023_paper.html)]
- **[CrowdCLIP]** CrowdCLIP: Unsupervised Crowd Counting via Vision-Language Model. (**CVPR 2023**) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Liang_CrowdCLIP_Unsupervised_Crowd_Counting_via_Vision-Language_Model_CVPR_2023_paper.html)] [[Code](https://github.com/dk-liang/CrowdCLIP)]
- **[FRVCC]** Frame-Recurrent Video Crowd Counting. (**IEEE TCSVT 2023**) [[Paper](https://doi.org/10.1109/TCSVT.2023.3250946)]
- **[PET]** Point-Query Quadtree for Crowd Counting Localization and More. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Point-Query_Quadtree_for_Crowd_Counting_Localization_and_More_ICCV_2023_paper.html)] [[Code](https://github.com/cxliu0/PET)]
- **[STEERER]** STEERER: Resolving Scale Variations for Counting and Localization via Selective Inheritance Learning. (**ICCV 2023**) [[Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Han_STEERER_Resolving_Scale_Variations_for_Counting_and_Localization_via_Selective_ICCV_2023_paper.html)] [[Code](https://github.com/taohan10200/STEERER)]

#### 2021

- **[P2PNet]** Rethinking Counting and Localization in Crowds: A Purely Point-Based Framework. (**ICCV 2021**) [[Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Song_Rethinking_Counting_and_Localization_in_Crowds_A_Purely_Point-Based_Framework_ICCV_2021_paper.html)] [[Code](https://github.com/TencentYoutuResearch/CrowdCounting-P2PNet)]

#### 2020

- **[DM-Count]** Distribution Matching for Crowd Counting. (**NeurIPS 2020**) [[Paper](https://proceedings.neurips.cc/paper/2020/hash/118bd558033a1016fcc82560c65cca5f-Abstract.html)] [[Code](https://github.com/cvlab-stonybrook/DM-Count)]

#### 2019

- **[BL]** Bayesian Loss for Crowd Count Estimation with Point Supervision. (**ICCV 2019**) [[Paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Ma_Bayesian_Loss_for_Crowd_Count_Estimation_With_Point_Supervision_ICCV_2019_paper.html)] [[Code](https://github.com/ZhihengCV/Bayesian-Crowd-Counting)]

#### 2018

- **[CSRNet]** CSRNet: Dilated Convolutional Neural Networks for Understanding the Highly Congested Scenes. (**CVPR 2018**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Li_CSRNet_Dilated_Convolutional_CVPR_2018_paper.html)] [[Code](https://github.com/leeyeehoo/CSRNet-pytorch)]
- **[FCRN]** Microscopy Cell Counting and Detection with Fully Convolutional Regression Networks. (**Computer Methods in Biomechanics and Biomedical Engineering: Imaging and Visualization 2018**) [[Paper](https://doi.org/10.1080/21681163.2016.1149104)]
- **[PhenoDC]** Pheno-Deep Counter: A Unified and Versatile Deep Learning Architecture for Leaf Counting. (**The Plant Journal 2018**) [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6282617/)] [[Code](https://bitbucket.org/tuttoweb/pheno-deep-counter)]
- **[LCFCN]** Where Are the Blobs: Counting by Localization with Point Supervision. (**ECCV 2018**) [[Paper](https://www.ecva.net/papers/eccv_2018/papers_ECCV/papers/Issam_Hadj_Laradji_Where_are_the_ECCV_2018_paper.pdf)] [[Code](https://github.com/ElementAI/LCFCN)]

#### 2017

- **[Count-ception]** Count-ception: Counting by Fully Convolutional Redundant Counting. (**ICCV Workshops 2017**) [[Paper](https://openaccess.thecvf.com/content_ICCV_2017_workshops/w1/html/Cohen_Count-ception_Counting_by_ICCV_2017_paper.html)] [[Code](https://github.com/ieee8023/countception)]
- **[Aso-sub]** Counting Everyday Objects in Everyday Scenes. (**CVPR 2017**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Chattopadhyay_Counting_Everyday_Objects_CVPR_2017_paper.html)]
- **[LPN]** Drone-Based Object Counting by Spatially Regularized Regional Proposal Network. (**ICCV 2017**) [[Paper](https://openaccess.thecvf.com/content_iccv_2017/html/Hsieh_Drone-Based_Object_Counting_ICCV_2017_paper.html)]

#### 2016

- **[COWC]** A Large Contextual Dataset for Classification Detection and Counting of Cars with Deep Learning. (**ECCV 2016**) [[Paper](https://link.springer.com/chapter/10.1007/978-3-319-46487-9_48)]
- **[Arteta et al. (2016)]** Counting in the Wild. (**ECCV 2016**) [[Paper](https://doi.org/10.1007/978-3-319-46478-7_30)]
- **[MCNN]** Single-Image Crowd Counting via Multi-Column Convolutional Neural Network. (**CVPR 2016**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2016/html/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.html)]

#### 2015

- **[Zhang et al. (2015)]** Cross-Scene Crowd Counting via Deep Convolutional Neural Networks. (**CVPR 2015**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2015/html/Zhang_Cross-Scene_Crowd_Counting_2015_CVPR_paper.html)]
- **[CVPPP Leaf Counting]** Learning to Count Leaves in Rosette Plants. (**CVPPP Workshop at BMVC 2015**) [[Paper](https://vios.science/assets/pdfs/Giuffrida_CVPPP2015.pdf)]

#### 2014

- **[Arteta et al. (2014)]** Interactive Object Counting. (**ECCV 2014**) [[Paper](https://doi.org/10.1007/978-3-319-10578-9_33)] [[Code](https://robots.ox.ac.uk/~vgg/research/counting/index.html)]

#### 2013

- **[Idrees et al.]** Multi-source Multi-scale Counting in Extremely Dense Crowd Images. (**CVPR 2013**) [[Paper](https://openaccess.thecvf.com/content_cvpr_2013/html/Idrees_Multi-source_Multi-scale_Counting_2013_CVPR_paper.html)]

#### 2010

- **[Lempitsky et al.]** Learning To Count Objects in Images. (**NeurIPS 2010**) [[Paper](https://proceedings.neurips.cc/paper/2010/hash/fe73f687e5bc5280214e0486b273a5f9-Abstract.html)] [[Code](https://robots.ox.ac.uk/~vgg/research/counting/index.html)]

### Video Object Counting

*10 papers.*

#### 2026

- **[Shu et al.]** Adapting Lightweight Image-Based Counting Models for Video Crowd Counting. (**CVPR 2026**) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shu_Adapting_Lightweight_Image-based_Counting_Models_for_Video_Crowd_Counting_CVPR_2026_paper.html)]
- **[DG-Det]** Depth-Guided Video Object Counting in Crowded Scenes. (**ACM MM 2026**) [[Paper](https://arxiv.org/abs/2608.06236)] [[Code](https://github.com/streamer-AP/DG-Net)]
- **[EC-Bench]** EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos. (**arXiv 2026**) [[Paper](https://arxiv.org/abs/2603.29943)]
- **[KBTrack]** KBTrack: cloud-enabled temporal identity inference for accurate counting in ornamental plant inventory management. (**Computers and Electronics in Agriculture 2026**) [[Paper](https://doi.org/10.1016/j.compag.2026.112307)]
- **[CountVid]** Open-World Object Counting in Videos. (**AAAI 2026**) [[Paper](https://arxiv.org/abs/2506.15368)] [[Code](https://github.com/niki-amini-naieni/CountVid)]
- **[SVCBench]** SVCBench: A Streaming Video Counting Benchmark for Spatial-Temporal State Maintenance. (**ECCV 2026**) [[Paper](https://arxiv.org/abs/2603.12703)] [[Code](https://buaa-colalab.github.io/SVCBench/)]

#### 2025

- **[AV-Reasoner]** AV-Reasoner: Improving and Benchmarking Clue-Grounded Audio-Visual Counting for MLLMs. (**arXiv 2025**) [[Paper](https://arxiv.org/abs/2506.05328)] [[Code](https://github.com/AV-Reasoner/AV-Reasoner)]
- **[E-MAC]** Efficient Masked AutoEncoder for Video Object Counting and A Large-Scale Benchmark. (**ICLR 2025**) [[Paper](https://openreview.net/forum?id=sY3anJ8C68)] [[Code](https://github.com/mast1ren/E-MAC)]
- **[SDNet]** Video Individual Counting for Moving Drones. (**ICCV 2025**) [[Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Video_Individual_Counting_for_Moving_Drones_ICCV_2025_paper.html)] [[Code](https://github.com/fyw1999/MovingDroneCrowd)]

#### 2023

- **[FRVCC]** Frame-Recurrent Video Crowd Counting. (**IEEE TCSVT 2023**) [[Paper](https://doi.org/10.1109/TCSVT.2023.3250946)]

## Leaderboard

Lower is better for MAE, RMSE, and NAE. Results are only ranked inside the same evaluation protocol; prompts, training data, annotations, splits, and output types can make numbers incomparable.

### FSC-147

The standard table below uses the original FSC-147 test annotations and three visual exemplars. Other protocols are separated into expandable tables. Full provenance and protocol notes are available in [data/leaderboard_fsc147.csv](data/leaderboard_fsc147.csv).

#### Standard 3-shot, FSC-147-trained

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| DAVE-density | **CVPR 2024** | 3 visual exemplars | FSC-147 test | 8.66 | 32.36 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.pdf) |
| CACViT | **AAAI 2024** | 3 visual exemplars | FSC-147 test | 9.13 | 48.96 | [Source](https://ojs.aaai.org/index.php/AAAI/article/view/28396) |
| LOCA | **ICCV 2023** | 3 visual exemplars | FSC-147 test | 10.79 | 56.97 | [Source](https://openaccess.thecvf.com/content/ICCV2023/papers/Dukic_A_Low-Shot_Object_Counting_Network_With_Iterative_Prototype_Adaptation_ICCV_2023_paper.pdf) |
| CounTR | **BMVC 2022** | 3 visual exemplars | FSC-147 test | 11.95 | 91.23 | [Source](https://www.robots.ox.ac.uk/~vgg/publications/2022/Liu22/liu22.pdf) |
| SAFECount | **WACV 2023** | 3 visual exemplars | FSC-147 test | 14.32 | 85.54 | [Source](https://openaccess.thecvf.com/content/WACV2023/papers/You_Few-Shot_Object_Counting_With_Similarity-Aware_Feature_Enhancement_WACV_2023_paper.pdf) |
| BMNet+ | **CVPR 2022** | 3 visual exemplars | FSC-147 test | 14.62 | 91.83 | [Source](https://openaccess.thecvf.com/content/CVPR2022/papers/Shi_Represent_Compare_and_Learn_A_Similarity-Aware_Framework_for_Class-Agnostic_Counting_CVPR_2022_paper.pdf) |
| FamNet | **CVPR 2021** | 3 visual exemplars | FSC-147 test | 22.08 | 99.54 | [Source](https://openaccess.thecvf.com/content/CVPR2021/papers/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.pdf) |

<details>
<summary><b>Text-only counting with standard FSC-147 annotations (13 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| CountSE | **ICCV 2025** | text only; internally generated soft exemplars | FSC-147 test | 7.84 | 82.99 | [Source](https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_CountSE_Soft_Exemplar_Open-set_Object_Counting_ICCV_2025_paper.pdf) |
| GroundingREC | **CVPR 2024** | referring-expression text | FSC-147 test | 10.12 | 107.19 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Dai_Referring_Expression_Counting_CVPR_2024_paper.pdf) |
| T2ICount | **CVPR 2025** | text class name | FSC-147 test | 11.76 | 97.86 | [Source](https://openaccess.thecvf.com/content/CVPR2025/papers/Qian_T2ICount_Enhancing_Cross-modal_Understanding_for_Zero-Shot_Counting_CVPR_2025_paper.pdf) |
| QICA-ViT-L/14 | **CVPR 2026** | text class name | FSC-147 test | 12.41 | 97.28 | [Source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Boosting_Quantitive_and_Spatial_Awareness_for_Zero-Shot_Object_Counting_CVPR_2026_paper.pdf) |
| QICA-ViT-B/16 | **CVPR 2026** | text class name | FSC-147 test | 13.05 | 104.17 | [Source](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Boosting_Quantitive_and_Spatial_Awareness_for_Zero-Shot_Object_Counting_CVPR_2026_paper.pdf) |
| CountGDtxt | **NeurIPS 2024** | text only | FSC-147 test | 14.76 | 120.42 | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c56985d9afe89bf78a8264c91071aa-Paper-Conference.pdf) |
| DAVEprm | **CVPR 2024** | text class prompt | FSC-147 test | 14.9 | 103.42 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.pdf) |
| CounTX-class-name | **BMVC 2023** | original FSC-147 class name | FSC-147 test | 15.73 | 106.88 | [Source](https://papers.bmvc2023.org/0510.pdf) |
| CounTX-description | **BMVC 2023** | FSC-147-D rich text description | FSC-147 test | 15.88 | 106.29 | [Source](https://papers.bmvc2023.org/0510.pdf) |
| VLCounter | **AAAI 2024** | text class name | FSC-147 test | 17.05 | 106.16 | [Source](https://ojs.aaai.org/index.php/AAAI/article/view/28050) |
| CLIP-Count | **ACM MM 2023** | text class name | FSC-147 test | 17.78 | 106.62 | [Source](https://arxiv.org/pdf/2305.07304) |
| VA-Count | **ECCV 2024** | text class name | FSC-147 test | 17.88 | 129.31 | [Source](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00812.pdf) |
| ZSC | **CVPR 2023** | text class name | FSC-147 test | 22.09 | 115.17 | [Source](https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_Zero-Shot_Object_Counting_CVPR_2023_paper.pdf) |

</details>

<details>
<summary><b>Multimodal prompting with standard FSC-147 annotations (1 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| CountGD | **NeurIPS 2024** | 3 visual exemplars plus text | FSC-147 test | 6.75 | 43.65 | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c56985d9afe89bf78a8264c91071aa-Paper-Conference.pdf) |

</details>

<details>
<summary><b>Reference-less counting without a user prompt (3 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| CounTR-0shot | **BMVC 2022** | no exemplar and no text | FSC-147 test | 14.12 | 108.01 | [Source](https://www.robots.ox.ac.uk/~vgg/publications/2022/Liu22/liu22.pdf) |
| DAVE-0shot | **CVPR 2024** | no exemplar and no text | FSC-147 test | 15.14 | 103.49 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.pdf) |
| LOCA-0shot | **ICCV 2023** | no exemplar and no text | FSC-147 test | 16.22 | 103.96 | [Source](https://openaccess.thecvf.com/content/ICCV2023/papers/Dukic_A_Low-Shot_Object_Counting_Network_With_Iterative_Prototype_Adaptation_ICCV_2023_paper.pdf) |

</details>

<details>
<summary><b>One-shot exemplar-based counting (2 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| DAVE-1shot | **CVPR 2024** | 1 visual exemplar | FSC-147 test | 11.29 | 66.36 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.pdf) |
| LOCA-1shot | **ICCV 2023** | 1 visual exemplar | FSC-147 test | 12.53 | 75.32 | [Source](https://openaccess.thecvf.com/content/ICCV2023/papers/Dukic_A_Low-Shot_Object_Counting_Network_With_Iterative_Prototype_Adaptation_ICCV_2023_paper.pdf) |

</details>

<details>
<summary><b>One-shot counting with detection-based evaluation (1 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| GeCo-1shot | **NeurIPS 2024** | 1 visual exemplar | FSC-147 test | 8.1 | 60.16 | [Source](https://papers.nips.cc/paper_files/paper/2024/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf) |

</details>

<details>
<summary><b>Detection-output counting under the strict protocol (3 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| GeCo | **NeurIPS 2024** | 3 visual exemplars | FSC-147 test | 7.91 | 54.28 | [Source](https://papers.nips.cc/paper_files/paper/2024/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf) |
| DAVEbox | **CVPR 2024** | 3 visual exemplars | FSC-147 test | 10.45 | 74.51 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Pelhan_DAVE_-_A_Detect-and-Verify_Paradigm_for_Low-Shot_Counting_CVPR_2024_paper.pdf) |
| PseCo | **CVPR 2024** | 3 visual exemplars | FSC-147 test | 13.05 | 112.86 | [Source](https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_Point_Segment_and_Count_A_Generalized_Framework_for_Object_Counting_CVPR_2024_paper.pdf) |

</details>

<details>
<summary><b>Reference-less detection-output counting (1 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| GeCo-0shot | **NeurIPS 2024** | no exemplar and no text | FSC-147 test | 13.3 | 108.72 | [Source](https://papers.nips.cc/paper_files/paper/2024/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf) |

</details>

<details>
<summary><b>Training-free counting with 3 exemplars (2 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| CountingDINO-DINOv2-ViT-L/14-reg | **WACV 2026** | 3 visual exemplars | FSC-147 test | 20.93 | 71.37 | [Source](https://openaccess.thecvf.com/content/WACV2026/papers/Pacini_CountingDINO_A_Training-free_Pipeline_for_Class-Agnostic_Counting_using_Unsupervised_Backbones_WACV_2026_paper.pdf) |
| CountingDINO-DINO-ViT-B/8 | **WACV 2026** | 3 visual exemplars | FSC-147 test | 30.05 | 90.3 | [Source](https://openaccess.thecvf.com/content/WACV2026/papers/Pacini_CountingDINO_A_Training-free_Pipeline_for_Class-Agnostic_Counting_using_Unsupervised_Backbones_WACV_2026_paper.pdf) |

</details>

<details>
<summary><b>Modified splits or corrected annotations (4 results)</b></summary>

| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |
|---|---|---|---|---:|---:|---|
| CountGD-star | **NeurIPS 2024** | 3 visual exemplars plus text | corrected FSC-147 test | 5.74 | 24.09 | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c56985d9afe89bf78a8264c91071aa-Paper-Conference.pdf) |
| CounTR-E3-no7171 | **BMVC 2022** | 3 visual exemplars | modified FSC-147 test | 11.22 | 87.68 | [Source](https://www.robots.ox.ac.uk/~vgg/publications/2022/Liu22/liu22.pdf) |
| CountGDtxt-star | **NeurIPS 2024** | text only | corrected FSC-147 test | 12.98 | 98.35 | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c56985d9afe89bf78a8264c91071aa-Paper-Conference.pdf) |
| CounTX-description-star | **BMVC / CountGD reevaluation 2024** | rich text description | corrected FSC-147 test | 15.69 | 106.06 | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c56985d9afe89bf78a8264c91071aa-Paper-Conference.pdf) |

</details>

### CLOC

This is the official static **CLOC-v1.1 corrected-test** snapshot. It must not be mixed with results reported on the original annotation version, and CLOC currently has no public submission server. Full per-domain values and provenance are in [data/leaderboard_cloc.csv](data/leaderboard_cloc.csv).

| Method | Venue | MAE ↓ | RMSE ↓ | NAE ↓ | Source |
|---|---|---:|---:|---:|---|
| Count Anything | **arXiv 2026** | 8.39 | 32 | 0.65 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| CountGD++ | **CVPR 2026** | 22.01 | 122.75 | 0.95 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| SAM3 | **ICLR 2026** | 25.65 | 132.07 | 0.85 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| CountSE | **ICCV 2025** | 27.14 | 130.03 | 2.16 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| VLCounter | **AAAI 2024** | 30.24 | 123.09 | 3.06 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| CLIP-Count | **ACM MM 2023** | 30.97 | 119.65 | 4.48 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| CounTX | **BMVC 2023** | 31.79 | 123.17 | 4.74 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| LocateAnything-3B | **arXiv 2026** | 32.43 | 144.35 | 0.71 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| YOLO-Count | **ICCV 2025** | 33.28 | 133.66 | 1.08 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| VA-Count | **ECCV 2024** | 33.81 | 130.73 | 4.59 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| YOLO-World-X | **CVPR 2024** | 35.06 | 140.19 | 0.76 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| GrdDINO-SwinB | **ECCV 2024** | 35.19 | 141.32 | 0.78 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| GLIP-L | **CVPR 2022** | 37.58 | 141.95 | 0.81 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| YOLOE-v8L | **ICCV 2025** | 40.21 | 142.47 | 0.99 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| YOLOE-11L | **ICCV 2025** | 40.24 | 142.46 | 1 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| T2ICount | **CVPR 2025** | 49.7 | 156.97 | 8.83 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| CountGD | **NeurIPS 2024** | 56.62 | 1099.56 | 5.17 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |
| LOCA | **ICCV 2023** | 68.09 | 179.34 | 14.7 | [Source](https://github.com/Mengqi-Lei/count-anything/blob/main/assets/readme/cloc_v1_1_main_results_table.png) |

<details>
<summary><b>CLOC-v1.1 per-domain MAE</b></summary>

| Method | General Scene | Remote Sensing | Histopathology | Cellular Microscopy | Agriculture | Microbiology |
|---|---:|---:|---:|---:|---:|---:|
| Count Anything | 7.36 | 6.19 | 16.64 | 38.65 | 41.78 | 4.3 |
| CountGD++ | 12.08 | 10.69 | 55.83 | 222.25 | 321.99 | 43.8 |
| SAM3 | 18.85 | 10.88 | 64.32 | 152.45 | 315.88 | 37.04 |
| CountSE | 19.4 | 19.08 | 70.27 | 120.08 | 302.19 | 22.22 |
| VLCounter | 22.85 | 22.46 | 55.14 | 125.83 | 306.38 | 37.72 |
| CLIP-Count | 23.28 | 25.82 | 57.98 | 121.17 | 298.45 | 22.4 |
| CounTX | 22.79 | 30.07 | 64.64 | 112.22 | 301.1 | 27.41 |
| LocateAnything-3B | 26.96 | 12.36 | 76 | 198.35 | 305.21 | 31.18 |
| YOLO-Count | 23.95 | 27.7 | 72.5 | 168.37 | 309.3 | 24.33 |
| VA-Count | 21.84 | 36.42 | 72.5 | 163.73 | 315.23 | 20.47 |
| YOLO-World-X | 28.02 | 17.81 | 67.93 | 226.07 | 321.13 | 42.49 |
| GrdDINO-SwinB | 29.41 | 14.14 | 69.11 | 224.96 | 320.17 | 43.75 |
| GLIP-L | 31.05 | 19.57 | 68.78 | 225.42 | 320.85 | 43.71 |
| YOLOE-v8L | 33.94 | 21.78 | 69.99 | 228.28 | 321.97 | 44.8 |
| YOLOE-11L | 33.98 | 21.79 | 69.95 | 228.24 | 321.88 | 44.81 |
| T2ICount | 32.85 | 62.48 | 73.06 | 151.3 | 296.37 | 203.51 |
| CountGD | 54.75 | 42.25 | 99.69 | 114.5 | 244.8 | 11.09 |
| LOCA | 53.45 | 81.41 | 65.86 | 124.36 | 473.81 | 39.47 |

</details>

## Tutorials and Blogs

### Surveys

- [A Survey on Class-Agnostic Counting: Advancements from Reference-Based to Open-World Text-Guided Approaches](https://arxiv.org/abs/2501.19184) — Jiang et al., 2026.
- [Object Counting Across Modalities: Taxonomies, Benchmarks, Applications, and Open Challenges](https://arxiv.org/abs/2608.23845) — Owusu and Sheshappanavar, 2026.
- [Deep Learning in Crowd Counting: A Survey](https://doi.org/10.1049/cit2.12241) — Sindagi et al., 2024.
- [Revisiting Crowd Counting: State-of-the-art, Trends, and Future Perspectives](https://arxiv.org/abs/2209.07271) — Khan et al., 2023.
- [A Survey on Deep Learning-Based Single Image Crowd Counting: Network Design, Loss Function and Supervisory Signal](https://doi.org/10.1016/j.neucom.2022.08.037) — Fan et al., 2022.
- [Survey on Deep Learning Based Crowd Counting](https://doi.org/10.7544/issn1000-1239.2021.20200699) — Journal of Computer Research and Development, 2021.
- [CNN-based Density Estimation and Crowd Counting: A Survey](https://arxiv.org/abs/2003.12783) — Gao et al., 2020.

### Project Pages and Official Guides

- [Count Anything](https://mengqi-lei.github.io/count-anything-projectpage/) — Lei et al., 2026.
- [CountVid: Open-World Object Counting in Videos](https://www.robots.ox.ac.uk/~vgg/research/countvid/) — Visual Geometry Group, University of Oxford, 2026.
- [CountGD: Multi-Modal Open-World Counting](https://www.robots.ox.ac.uk/~vgg/research/countgd/) — Visual Geometry Group, University of Oxford, 2024.
- [CounTX: Open-world Text-specified Object Counting](https://www.robots.ox.ac.uk/~vgg/research/countx/) — Visual Geometry Group, University of Oxford, 2023.
- [Learning To Count Everything (FamNet)](https://github.com/cvlab-stonybrook/LearningToCountEverything) — Stony Brook CVLab, 2021.
- [Class-Agnostic Counting](https://www.robots.ox.ac.uk/~vgg/research/class-agnostic-counting/) — Visual Geometry Group, University of Oxford, 2018.
- [Learning to Count Objects in Images](https://www.robots.ox.ac.uk/~vgg/research/counting/index.html) — Visual Geometry Group, University of Oxford, 2010.

### Curated Lists and Engineering Tutorials

- [Object Counting using Ultralytics YOLO](https://docs.ultralytics.com/guides/object-counting/) — Ultralytics, 2023.
- [Awesome Crowd Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) — Community / gjy3035, 2019.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for scope, metadata, verification, and formatting requirements. Additions should update the structured CSV first and then regenerate this README.

## License

This repository is released under the [Apache License 2.0](LICENSE).
