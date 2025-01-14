"""Apply registration of image to a reference image."""

import os
import subprocess
import numpy as np
import nibabel as nb

# =============================================================================
REFEFENCE = "/Users/faruk/data/video-siham/video/03_baby_MNI_templates/01_upsample/nihpd_asym_00-02_t1w_resamp-0pt5.nii.gz"

IN_NAMES = [
    "/Users/faruk/data/video-siham/video/02_ROIs/CC00505XX10_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01020XX06_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01022XX08_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01034XX12_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01037XX15_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01059BN12_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01069XX14_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01093AN14_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01093BN14_seg_refT1.nii",
    "/Users/faruk/data/video-siham/video/02_ROIs/CC01104XX07_seg_refT1.nii",
    ]

AFFINES = [
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC00505XX10_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01020XX06_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01022XX08_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01034XX12_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01037XX15_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01059BN12_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01069XX14_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01093AN14_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01093BN14_to_template.mat",
     "/Users/faruk/data/video-siham/video/04_registration_affines/sub-CC01104XX07_to_template.mat",
    ]

OUTDIR = "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs"

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
print("  Output directory: {}\n".format(OUTDIR))

# =============================================================================
for i in range(len(IN_NAMES)):
        print(f"  Applying registration for image {i+1}")

        # Prepare output
        basename, ext = IN_NAMES[i].split(os.extsep, 1)
        basename = os.path.basename(basename)
        print(basename)
        out_moving = os.path.join(OUTDIR, "{}_reg.nii.gz".format(basename))

        # Prepare command
        command = "greedy "
        command += "-d 3 "
        command += "-rf {} ".format(REFEFENCE)
        command += "-ri LABEL 0.5vox "  # interpolation mode for subsequent -rm commands
        command += "-rm {} {} ".format(IN_NAMES[i], out_moving)  # moving resliced
        command += "-r {} ".format(AFFINES[i])  # sequence of transformations, from last to first

        # Execute command
        print("\n" + command + "\n")
        subprocess.run(command, shell=True, check=True)

print('Finished.')
