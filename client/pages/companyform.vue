<template>
  <v-container>
    <v-toolbar-title>Publish a Hackathon</v-toolbar-title>
    <v-divider></v-divider>
    <div class="d-flex">
      <v-btn text :class="{ highlight: currentPage === 'publish' }">
        Publish a Hackathon
      </v-btn>
      <v-btn
        text
        :class="{ highlight: currentPage === 'leaderboard' }"
        to="/leaderboard"
      >
        Leaderboard
      </v-btn>
      <v-btn
        text
        :class="{ highlight: currentPage === 'dashboard' }"
        to="/companyhackathon"
      >
        Dashboard
      </v-btn>
    </div>
    <v-layout row class="mt-4">
      <v-flex xs6>
        <v-card class="mb-4">
          <v-card-title class="justify-start">Name Of Hackathon</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-text-field
              v-model="hackathonName"
              label="Hackathon Name"
              outlined
            />
          </v-card-text>
        </v-card>
        <v-card class="mb-4">
          <v-card-title class="justify-start">Rewards</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-layout align-center>
              <v-btn @click="decrementReward" icon>
                <v-icon>mdi-minus</v-icon>
              </v-btn>
              <v-text-field
                v-model="reward"
                label="Rewards"
                outlined
              ></v-text-field>
              <v-btn @click="incrementReward" icon>
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs6>
        <v-card class="mb-4 ml-4" style="height: 320px">
          <v-card-title class="justify-start">Description</v-card-title>
          <v-divider></v-divider>
          <v-card-text class="mt-8">
            <v-textarea
              outlined
              v-model="hackathonDescription"
              rows="5"
              ref="textarea"
              @input="adjustTextareaHeight"
            />
          </v-card-text>
        </v-card>
      </v-flex>
      <v-card class="mb-4" style="width: 100%">
        <v-card-title class="privacy_title">Privacy</v-card-title>
        <v-divider></v-divider>
        <v-card-subtitle class="text-left"
          >Choose who can access your hackathon</v-card-subtitle
        >
        <v-card-text class="justify-end">
          <v-btn-toggle v-model="visibility">
            <v-btn value="public">Public</v-btn>
            <v-btn value="private">Private</v-btn>
          </v-btn-toggle>
        </v-card-text>
      </v-card>
      <v-flex xs6>
        <v-card class="mb-4 mr-4" style="height: 300px">
          <v-card-title class="justify-start">Problem Statement</v-card-title>
          <v-divider></v-divider>
          <v-card-text class="mt-8">
            <v-textarea
              outlined
              v-model="problemStatement"
              rows="5"
              ref="textarea"
              @input="adjustTextareaHeight"
            />
          </v-card-text>
        </v-card>
        <v-card class="mb-4 mr-4">
          <v-card-title class="justify-start">External Links</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-text-field v-model="links" label="Links" outlined
          /></v-card-text>
        </v-card>
        <v-card>
          <v-card-title class="justify-start">
            Publish Your Hackathon
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-btn outlined @click="startHackathon">Publish</v-btn>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs6>
        <v-card class="mb-4">
          <v-card-title class="justify-start"> Date </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col cols="6">
                <v-date-picker v-model="startDate" label="Start Date" />
                
              </v-col>
              <v-col cols="6">
                
                <v-date-picker v-model="endDate" label="End Date" />
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import axios from "axios";
// import moment from "moment";
import { format } from "date-fns";
export default {
  data() {
    return {
      hackathonName: "",
      hackathonDescription: "",
      startDate: null,
      endDate: null,
      problemStatement: "",
      visibility: "public",
      reward: 1000,
      links: "",
      currentPage: "publish",
    };
  },
  methods: {
    adjustRewards(action) {
      if (action === "up") {
        this.reward += 100;
      } else if (action === "down") {
        this.reward -= 100;
      }
    },
    adjustTextareaHeight() {
      this.$nextTick(() => {
        const textareaHeight = this.$refs.textarea.$el.scrollHeight;
        this.hackathonDescriptionHeight = `${textareaHeight}px`;
      });
    },
    startHackathon() {
      // const formattedStartDate = format(this.startDate, 'yyyy-MM-dd');
      // const formattedEndDate = format(this.endDate, "yyyy-MM-dd");
      const data = {
        name: this.hackathonName,
        end_date: this.endDate,
        start_date: this.startDate,
        visibility: this.visibility,
        description: this.hackathonDescription,
        problem_statements: this.problemStatement,
        Reward : this.reward,
        // Include other properties as needed
      };
      console.log(data)
      axios
        .post("http://127.0.0.1:8000/hackathons/create/", data)
        .then((response) => {
          console.log("API Response:", response);
          this.$router.push("/companyhackathon");
        })
        .catch((error) => {
          console.error("Error posting data:", error);
        });
    },
    incrementReward() {
      this.reward++;
    },
    decrementReward() {
      if (this.reward > 0) {
        this.reward--;
      }
    },
  },
};
</script>
<style scoped>
.privacy_title {
  justify-content: flex-start;
}
.highlight {
  color: #0000cc; /* Dark blue color */
  font-weight: bold;
}
</style>
