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
