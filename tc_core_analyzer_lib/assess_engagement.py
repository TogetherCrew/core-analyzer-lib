# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  assess_engagement.py
#
#  Author Ene SS Rawa / Tjitse van der Molen

from .utils.assessments import (  # isort: skip
    assess_active,
    assess_connected,
    assess_consistent,
    assess_dropped,
    assess_lurker,
    assess_overlap,
    assess_remainder,
    assess_still_active,
    assess_vital,
)
from .utils.compute_interaction_per_acc import thr_int


class EngagementAssessment:
    def __init__(
        self,
        activities: list[str],
        activities_ignore_0_axis: list[str],
        activities_ignore_1_axis: list[str],
    ) -> None:
        """
        The memberactivitie engagement assessment method

        Parameters:
        -------------
        activities : list[str]
            the activities that the interaction matrixes would have
        activities_ignore_0_axis : list[str]
            the activities that the 0 axis of their matrix
            won't be included in computations.
            Note: Could be an empty list
        activities_ignore_1_axis : list[str]
            the activities that the 1 axis of their matrix
            won't be included in computations.
            Note: Could be an empty list
        """

        self.activities = activities
        self.activities_ignore_0_axis = activities_ignore_0_axis
        self.activities_ignore_1_axis = activities_ignore_1_axis

    def compute(
        self,
        int_mat,
        w_i,
        acc_names,
        act_param,
        WINDOW_D,
        all_joined,
        all_joined_day,
        all_consistent,
        all_vital,
        all_active,
        all_connected,
        all_paused,
        all_new_disengaged,
        all_disengaged,
        all_unpaused,
        all_returned,
        all_new_active,
        all_still_active,
        all_dropped,
        all_disengaged_were_vital,
        all_disengaged_were_newly_active,
        all_disengaged_were_consistently_active,
        all_lurker,
        all_about_to_disengage,
        all_disengaged_in_past,
    ):
        """
        Assess engagment levels for all active members in a time period

        Parameters:
        ------------
        int_mat : dict[str, np.ndarray[int]]
            interaction matrix of activities of users,
            each activity has a 2D matrix
        activities : list[str]
            the activities which the interaction matrix has
            must include at list 1 activity
        w_i : int
            index of sliding time window
        WINDOW_D : int
            duration of sliding window (days)
        all_* : dict[str, set[str]]
            dictionary with keys w_i and values
            containing a list of all account names belonging to engagement
            category *

        act_param : dict[str, int]
            parameters for activity types:
            keys are listed below
                - INT_THR : int
                    minimum number of interactions to be active
                - UW_DEG_THR : int
                    minimum number of connections to be active
                - EDGE_STR_THR : int
                    minimum number of interactions for connected
                - UW_THR_DEG_THR : int
                    minimum number of accounts for connected
                - CON_T_THR : int
                    time period to assess consistently active
                - CON_O_THR : int
                    times to be active within CON_T_THR to be
                consistently active
                - VITAL_T_THR : int
                    time period to assess for vital
                - VITAL_O_THR : int
                    times to be connected within VITAL_T_THR to be vital
                - PAUSED_T_THR : int
                    time period to remain paused
                - STILL_T_THR : int
                    time period to assess for still active
                - STILL_O_THR : int
                    times to be active within STILL_T_THR to be still active
                - DROP_H_THR : int
                    time periods in the past to have been newly active
                - DROP_I_THR : int
                    time periods to have been inactive

        Returns:
        ---------
        graph : networkx.DiGraph
            networkx object for int_mat
        all_* : dict[str, [str]]
            dictionary with keys w_i and values
            containing a list of all account names belonging to engagement
            category * updated for window w_i
        all_disengaged_* : dict[str, set[str]]
            set with all unique account names belong to one of the
            disengaged member types for window w_i
        """

        # # # THRESHOLD INTERACTIONS # # #
        thr_ind, thr_uw_deg, thr_uw_thr_deg, graph = thr_int(
            int_mat,
            act_param["INT_THR"],
            act_param["UW_DEG_THR"],
            act_param["EDGE_STR_THR"],
            act_param["UW_THR_DEG_THR"],
            activities=self.activities,
            ignore_axis_0_activities=self.activities_ignore_0_axis,
            ignore_axis_1_activities=self.activities_ignore_1_axis,
        )

        # # # ACTIVE # # #

        all_active = assess_active(acc_names, thr_ind, thr_uw_deg, w_i, all_active)

        # # # # CONNECTED # # #

        all_connected = assess_connected(acc_names, thr_uw_thr_deg, w_i, all_connected)

        # # # CONSISTENTLY ACTIVE # # #

        all_consistent = assess_consistent(
            all_active,
            w_i,
            act_param["CON_T_THR"],
            act_param["CON_O_THR"],
            WINDOW_D,
            all_consistent,
        )

        # # # VITAL # # #

        all_vital = assess_vital(
            all_connected,
            w_i,
            act_param["VITAL_T_THR"],
            act_param["VITAL_O_THR"],
            WINDOW_D,
            all_vital,
        )

        # # # STILL ACTIVE # # #

        all_still_active = assess_still_active(
            all_new_active,
            all_active,
            w_i,
            act_param["STILL_T_THR"],
            act_param["STILL_O_THR"],
            WINDOW_D,
            all_still_active,
        )

        # # # DROPPED # # #

        all_dropped = assess_dropped(
            all_new_active,
            all_active,
            w_i,
            act_param["DROP_H_THR"],
            act_param["DROP_I_THR"],
            WINDOW_D,
            all_dropped,
        )

        # # # REMAINDER # # #

        (
            all_new_active,
            all_unpaused,
            all_returned,
            all_paused,
            all_new_disengaged,
            all_disengaged,
            all_disengaged_in_past,
        ) = assess_remainder(
            all_active,
            w_i,
            WINDOW_D,
            act_param["PAUSED_T_THR"],
            all_new_active,
            all_unpaused,
            all_returned,
            all_paused,
            all_new_disengaged,
            all_disengaged,
            all_disengaged_in_past,
        )

        # # # LURKER # # #

        all_lurker = assess_lurker(
            all_lurker,
            all_new_active,
            all_joined_day,
            w_i,
        )

        # # # ABOUT TO DISENGAGE # # #

        all_about_to_disengage[str(w_i)] = (
            all_paused[str(w_i)] - all_consistent[str(w_i)]
        )

        # # # SUBDIVIDE DISENGAGED TYPES # # #

        # make temporary dictionary for remaining disengaged members
        rem_new_disengaged = {}

        # if there is any disengagement data
        if str(w_i) in all_new_disengaged.keys():
            # assess who was core before they disengaged
            (
                rem_new_disengaged[str(w_i)],
                all_disengaged_were_vital[str(w_i)],
            ) = assess_overlap(
                all_new_disengaged,
                all_vital,
                w_i,
                (act_param["PAUSED_T_THR"] + 1) * WINDOW_D,
            )

            # assess who of the remaining disengaged accounts
            # was consistently active before they disengaged
            (
                rem_new_disengaged[str(w_i)],
                all_disengaged_were_consistently_active[str(w_i)],
            ) = assess_overlap(
                rem_new_disengaged,
                all_consistent,
                w_i,
                (act_param["PAUSED_T_THR"] + 1) * WINDOW_D,
            )

            # assess who of the remaining disengaged accounts
            #  was newly active before they disengaged
            (
                rem_new_disengaged[str(w_i)],
                all_disengaged_were_newly_active[str(w_i)],
            ) = assess_overlap(
                rem_new_disengaged,
                all_new_active,
                w_i,
                (act_param["PAUSED_T_THR"] + 1) * WINDOW_D,
            )
        else:
            all_disengaged_were_vital[str(w_i)] = set()
            all_disengaged_were_consistently_active[str(w_i)] = set()
            all_disengaged_were_newly_active[str(w_i)] = set()

        return (
            graph,
            all_joined,
            all_joined_day,
            all_consistent,
            all_vital,
            all_active,
            all_connected,
            all_paused,
            all_new_disengaged,
            all_disengaged,
            all_unpaused,
            all_returned,
            all_new_active,
            all_still_active,
            all_dropped,
            all_disengaged_were_newly_active,
            all_disengaged_were_consistently_active,
            all_disengaged_were_vital,
            all_lurker,
            all_about_to_disengage,
            all_disengaged_in_past,
        )
