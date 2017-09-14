from csv import reader

dir_origin = "./Group and Catalogids_FI.csv"
dir_new = "./Group and Catalogids_FI_updated.csv"

def generateCSV(dir_origin):
    
    csv_new = []

    csv_origin = open(dir_origin, 'r')
    lines = reader(csv_origin)
    
    for line in lines:
        str_temp = ""
       
        AppName = '"' + line[0] + '"'
        ApplicationType = '"' + line[1] + '"'
        BusinessGroupName = '"' + line[3] + '"'
        BusinessGroupDescription = '"' + line[4] + '"'
        BusinessRoleName = '"' + line[5] + '"'
        BusinessRoleDescription = '"' + line[6] + '"'
        LeadingTransactionCodes = '"' + line[7] + '"'
        
        if ',' in line[2]:
            bcn_data = line[2].split(',')
            for i in range(0, len(bcn_data)):
                BusinessCatalogName = '"' + bcn_data[i] + '"'
                str_temp = AppName + "," + ApplicationType + "," + BusinessCatalogName + "," + BusinessGroupName + "," + BusinessGroupDescription + "," + BusinessRoleName + "," + BusinessRoleDescription + "," + LeadingTransactionCodes 
                csv_new.append(str_temp)
                #print(str_temp)
        else:
            BusinessCatalogName = '"' + line[2] + '"'
            str_temp = AppName + "," + ApplicationType + "," + BusinessCatalogName + "," + BusinessGroupName + "," + BusinessGroupDescription + "," + BusinessRoleName + "," + BusinessRoleDescription + "," + LeadingTransactionCodes 
            csv_new.append(str_temp)
            #print(str_temp)         
    
    csv_origin.close()
    
    fw = open(dir_new, 'w')
    for line in csv_new:
        fw.write(line + '\n')
    fw.close()

generateCSV(dir_origin)
