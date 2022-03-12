from autopilot.core.subject import Subject

# open subject file
sub = Subject('subject_id', dir='/mnt/ion-nas/autopilot/data')

# get dataframe of subject trial data
df = sub.get_trial_data('all')

for session, group in df.groupby('session'):
    group.to_csv(f'/output/location/subject_id_{session}.csv')


