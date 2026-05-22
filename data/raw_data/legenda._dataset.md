Fighter_Name: Full name of the fighter (Primary Key to join with the Fights dataset).

Height_cm: Fighter's height in centimeters.


Weight_kg: Fighter's official weight in kilograms.

Reach_cm: Fighter's reach (wingspan) in centimeters.

Stance: Combat stance (Orthodox, Southpaw, Switch).

DOB: Date of Birth (Datetime format).

Wins / Losses / Draws: Overall MMA career record at the time of data extraction.

SLpM: Significant Strikes Landed per Minute (Offensive volume).

Str_Acc: Striking Accuracy (Percentage of strikes that land).

SApM: Significant Strikes Absorbed per Minute (Defensive liability).

Str_Def: Striking Defense (Percentage of opponents' strikes avoided/blocked).

TD_Avg: Takedowns Average (Takedowns landed per 15 minutes).

TD_Acc: Takedown Accuracy (Percentage of takedown attempts that are successful).

TD_Def: Takedown Defense (Percentage of opponents' takedown attempts successfully defended).

Sub_Avg: Submission Average (Submissions attempted per 15 minutes).

Fighter_URL: Unique URL identifier for the fighter's profile.

Data Dictionary:
Fight_URL: Unique URL identifier for the fight.

Fighter_1 / Fighter_2: Names of the competing fighters.

Winner: Name of the winning fighter (or 'Draw/NC').

Weight_Class: The weight division of the bout (e.g., Lightweight Bout).

Method: Method of victory (e.g., KO/TKO, Decision - Unanimous, Submission).

End_Round: The round in which the fight ended.

End_Time: The exact clock time when the fight was stopped in the final round.

Total_Fight_Time_Sec: Total duration of the fight converted into pure seconds.

Time_Format: Scheduled format of the bout (e.g., 3 Rnd or 5 Rnd).

Event_Date: The date the event took place.

Performance Metrics (Prefix F1_ for Fighter 1, F2_ for Fighter 2):

_KD: Knockdowns scored.

_Sig_Landed / _Sig_Att: Significant strikes landed / attempted.

_TD_Landed / _TD_Att: Takedowns landed / attempted.

_Sub_Att: Submission attempts.

_Ctrl_Sec: Total control time on the ground or clinch, measured in seconds.
Strike Targets & Positions (Only Landed strikes are tracked here):

_Head / _Body / _Leg: Significant strikes landed to the head, body, and legs.

_Distance / _Clinch / _Ground: Significant strikes landed at a distance, in the clinch, and on the ground.
