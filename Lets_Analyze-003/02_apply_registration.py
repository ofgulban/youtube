"""Apply registration to an image."""

import os
import subprocess
import numpy as np
import nibabel as nb

# =============================================================================
REFEFENCE = "/Users/faruk/data/video-siham/video/03_baby_MNI_templates/01_upsample/nihpd_asym_00-02_t1w_resamp-0pt5.nii.gz"

IN_NAMES = [
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC00505XX10_ses-146900_rec-SVR_T1w_registered.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01020XX06_ses-72930_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01022XX08_ses-79430_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01034XX12_ses-51730_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01037XX15_ses-77430_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01059BN12_ses-72330_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01069XX14_ses-79730_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01093AN14_ses-75130_rec-SVR_T1w_registered.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01093BN14_ses-75230_rec-SVR_T1w.nii.gz",
    "/Users/faruk/data/video-siham/video/01_anatomicals_T1w/sub-CC01104XX07_ses-82830_rec-SVR_T1w_regis.nii.gz",
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

OUTDIR = "/Users/faruk/data/video-siham/video/05_apply_registration"

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
        command += "-ri LINEAR "  # interpolation mode for subsequent -rm commands
        command += "-rm {} {} ".format(IN_NAMES[i], out_moving)  # moving resliced
        command += "-r {} ".format(AFFINES[i])  # sequence of transformations, from last to first

        # Execute command
        print("\n" + command + "\n")
        subprocess.run(command, shell=True, check=True)

print('Finished.')
