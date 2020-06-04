score=X_test.tail(1)
scoring_data=list(list(x) for x in zip(*(score[x].values.tolist() for x in score.columns)))
fields=list(X_test.columns)
job_payload = {
client.deployments.ScoringMetaNames.INPUT_DATA: [{
 'values': scoring_data
}]
}
scoring_response = client.deployments.score(deployment_uid, job_payload)

print(scoring_response)
