FROM node:18

COPY . .

WORKDIR ./mobile-photo-frontend

RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve", "--lab-host=0.0.0.0", "--external", "--host=0.0.0.0"]
