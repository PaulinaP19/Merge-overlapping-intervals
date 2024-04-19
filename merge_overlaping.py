
source = "./GSE171116_N6mA_ChIPexo_noDup_hg38.sorted.cat.sort.bed"

def MergeChr(source):
    name_append = "_intersect4"
    target = source.rsplit(".", 1)
    target = target[0] + name_append + "." + target[1]
   
    
    merged_lines = []
    cluster = []
    new_line = True
    chromosome = ""

    with open(source) as f:
        for line_raw in f:
            line = line_raw.split("\t")[0:3]
            line[1] = int(line[1])
            line[2] = int(line[2])
           

            if new_line:
                chromosome = line[0]
                end = line[2]
                new_line = False

            if line[0] == chromosome and line[1] < end:
                if line[2] > end:
                    end = line[2]
                cluster.append(line)
            else:
                if len(cluster) > 1:
                    merged_lines.append(MergeCluster(cluster))
                else:
                   cluster = []
                chromosome = line[0]
                end = line[2]
                cluster = [line]
    
    with open(target, 'w') as f:
  
        for line in merged_lines:
           
            for i in range(2):
                f.write(str(line[i])+"\t")
            f.write(str(line[2]))
            f.write("\n")


def MergeCluster(cluster):
    end = cluster[0][2]
     
    for line in cluster:
        if end < line[2]:
            end = line[2]
       
    return [cluster[0][0], cluster[0][1], end]

MergeChr(source)
