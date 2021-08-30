from pyspark import SparkContext

logFile = "/Users/jingshuai/Downloads/spark-3.1.2-bin-hadoop3.2/README.md"
sc = SparkContext("local","Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
temp = logData.first()

print (temp)

print("Lines with a: %i, lines with b: %i"%(numAs, numBs))
