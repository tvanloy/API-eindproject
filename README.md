# API-eindproject
Voor dit project heb ik er voor gekozen om opnieuw te beginnen omdat ik tegen heel wat problemen stootte met mijn vorige API. Nu heb ik ervoor gekozen om een API te maken waarin je quotes kan plaatsen, bij deze quotes kan je dan de naamm van de persoon met die quote zetten. quotes kunnen verwijderd en geupdate worden.

# Endpoints
<ul> 
   <li>GET /users: Geeft alle Users weer met de quotes die zij gepost hebben.</li>
   <li>GET /users/{user_id}: Geeft een user weer op basis van een user id.</li>
   <li>GET /quotes: Geeft alle quotes die gepost zijn met de naam van wie deze gezegd heeft.</li>
   <li>GET /quotes/{quote_id}: Geeft een bepaalde quote weer op basis van het id van deze quote </li>
   <li>POST /users: Dit laat een persoon een user aanmaken met een email en een wachtwoord.</li>
   <li>POST /users/{user_id}/posts: Dit laat een user aan de hand van een user id een nieuwe post maken.</li>
   <li>POST /token: login voor toegang.</li>
   <li>PUT /quotes/{post_id}: Laat een gebruiker een post aanpassen.</li>
   <li>DELETE /quotes/{quote_id}: Laat een gebruiker een post verwijderen.</li>
</ul>


# OpenAPI docs
![image](https://user-images.githubusercontent.com/91123059/211206414-5672db66-777f-4546-908a-e65f5ebdc02a.png)
![image](https://user-images.githubusercontent.com/91123059/211206458-0ed6dd85-b63b-4f78-b720-a3b184a65cd0.png)
![image](https://user-images.githubusercontent.com/91123059/211206474-08e0a656-f33e-4f54-a5ae-a7ea3fb81134.png)
![image](https://user-images.githubusercontent.com/91123059/211206490-bdfba969-ad77-4f01-a334-b62b4501fb9f.png)
![image](https://user-images.githubusercontent.com/91123059/211206514-77ca8e1a-f5c6-4d56-ad78-ef808f7cde75.png)
![image](https://user-images.githubusercontent.com/91123059/211206525-c9aeebcf-49a3-4769-9538-3ddf62d8cd75.png)
![image](https://user-images.githubusercontent.com/91123059/211206537-48804871-f50a-4a27-a083-bf932b11a8be.png)
![image](https://user-images.githubusercontent.com/91123059/211206546-0794e184-c4e0-49cc-b6ef-36024a3cea41.png)
![image](https://user-images.githubusercontent.com/91123059/211206559-673762f9-6229-41ba-af9d-dc462a020b48.png)
![image](https://user-images.githubusercontent.com/91123059/211206570-91c7d72f-0a53-465d-81d7-b6484ea5acd9.png)

# Postman
![image](https://user-images.githubusercontent.com/91123059/211215634-8bbb8152-e360-4d24-9cf0-3c834e45f543.png)
![image](https://user-images.githubusercontent.com/91123059/211216389-75f0354e-8037-4092-9eee-42c1c6a8fa81.png)
![image](https://user-images.githubusercontent.com/91123059/211216451-574694e8-03f0-4411-a51f-77e824513761.png)
![image](https://user-images.githubusercontent.com/91123059/211220740-210e99fc-6639-43b2-94ac-f149bed2a5b8.png)
![image](https://user-images.githubusercontent.com/91123059/211220805-70ac638e-cb48-40cb-9212-13065ec2c306.png)
![image](https://user-images.githubusercontent.com/91123059/211220826-a950fed9-4335-4ea3-a9ae-9d99eccb2a81.png)
![image](https://user-images.githubusercontent.com/91123059/211220852-444a2019-9526-450b-ae38-66ac0fb9c8fb.png)
![image](https://user-images.githubusercontent.com/91123059/211220935-d17b9197-1d3d-4a47-aa36-88ed94ffd935.png)
![image](https://user-images.githubusercontent.com/91123059/211220942-5dc9a910-1d0a-4291-840b-b71ed6e0cb34.png)



