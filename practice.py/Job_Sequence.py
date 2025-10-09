def JobSequence(jobId,profite,deadline):

    n = len(jobId)
    maxdead = max(deadline)
    
    jobs = sorted(zip(profite,deadline,jobId),reverse=True)

    slot = ['0'] * (maxdead + 1)
    final_profite = 0

    for i in range (n): # for every decending jobs
        dl = jobs[i][1]
        for j in range(dl,0,-1):
            if slot[j] == '0':
                slot[j] = jobs[i][2]
                final_profite += jobs[i][0]
                break

    return [slot, final_profite]

if __name__ == "__main__":
    deadline = []
    profite = []
    jobId = []

    n = int(input("Give the number of the jobs : "))

    for i in range(n):
        job_id = input("Give the job id : ")
        jobId.append(job_id)
        pro = int(input("Give the profite : "))
        profite.append(pro)
        line = int(input("Give the deadline : "))
        deadline.append(line)

    ans = JobSequence(jobId,profite,deadline)

    print(f"The final jon sequence is : {ans[0][1:]}")
    print(f"The profite is {ans[1]}")