/*
 * Copyright (C) 2014, 2016 Karl Wette
 * Copyright (C) 2009-2013 Adam Mercer
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or (at
 * your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with with program; see the file COPYING. If not, write to the
 * Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
 * MA 02111-1307 USA
 */

/*
 * LALVCSInfo.h - LAL VCS Information Header
 */

/** \cond DONT_DOXYGEN */

#ifndef _LALVCSINFOHEADER_H
#define _LALVCSINFOHEADER_H

#include <lal/LALVCSInfoType.h>
#include <lal/LALVCSInfo.h>
#include <lal/LALConfig.h>

#ifdef __cplusplus
extern "C" {
#endif

/* VCS information */
#define LAL_VCS_ID "f1c13e21f6d66f7c1c83367f585289fcbe0a95f1"
#define LAL_VCS_DATE "2017-05-11 14:34:43 +0000"
#define LAL_VCS_BRANCH "minke"
#define LAL_VCS_TAG "None"
#define LAL_VCS_AUTHOR "Daniel Williams <mail@daniel-williams.co.uk>"
#define LAL_VCS_COMMITTER "Daniel Williams <mail@daniel-williams.co.uk>"
#define LAL_VCS_CLEAN "CLEAN"
#define LAL_VCS_STATUS "CLEAN: All modifications committed"

/* VCS header/library mismatch link check function */
#define LAL_VCS_LINK_CHECK LAL_CLEAN_f1c13e21f6d66f7c1c83367f585289fcbe0a95f1_VCS_HEADER_LIBRARY_MISMATCH
void LAL_VCS_LINK_CHECK(void);

#ifdef __cplusplus
}
#endif

#endif /* _LALVCSINFOHEADER_H */

/** \endcond */
