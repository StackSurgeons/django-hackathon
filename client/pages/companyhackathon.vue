<template>
  <v-container>
    <v-row class="justify-space-between">
      <v-col class="text-centerc" cols="12" sm="3">
        <v-card class="d-flex flex-column rounded-xl custom-border-dotted">
          <div class="d-flex">
            <v-card-text class="pa-0">
              <v-list-item-subtitle
                class="text-left pa-6"
                style="font-size: 25px"
                >Users <br />Registered <br />
                <div class="mt-2" style="font-size: 10px">
                  <v-icon>mdi-calendar</v-icon>22 June 2023
                </div>
              </v-list-item-subtitle>
            </v-card-text>
            <v-card-subtitle class="d-flex align-center" style="font-size: 15px"
              ><v-icon small class="subtitle-icon">mdi-bell</v-icon>
            </v-card-subtitle>
          </div>
          <div class="ma-4">
            <v-row class="avatar-row">
              <v-col
                v-for="(user, index) in displayedUsers"
                :key="index"
                cols="auto"
              >
                <v-avatar
                  v-if="user.isCount"
                  class="user-avatar remaining-count-avatar"
                  @click="showUserList = true"
                >
                  <span class="remaining-count">+{{ user.count }}</span>
                </v-avatar>
                <v-avatar
                  v-else
                  class="user-avatar"
                  :style="{
                    backgroundImage: `url(${user.profileImage})`,
                    borderColor: user.hasNewStory ? 'red' : 'transparent',
                  }"
                ></v-avatar>
              </v-col>
            </v-row>
          </div>
        </v-card>
      </v-col>
      <v-dialog v-model="showUserList" max-width="500px">
        <v-card>
          <v-card-title> Active Registered Users </v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item v-for="(user, index) in activeUsers" :key="index">
                <v-list-item-content>{{ user.user }}</v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="showUserList = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-col class="text-centerc" cols="12" sm="3">
        <v-card class="d-flex rounded-xl custom-border-dotted">
          <v-card-text>
            <v-list-item-subtitle class="mb-2" style="font-size: 25px"
              >Statistics
            </v-list-item-subtitle>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="text-center" cols="12" sm="3">
        <v-card class="d-flex flex-column rounded-xl custom-border-dotted">
          <v-card-text>
            <v-list-item-subtitle class="mb-2" style="font-size: 25px">
              Rewards
            </v-list-item-subtitle>
          </v-card-text>
          <v-list-item>+8%</v-list-item>
          <v-card-subtitle
            class="d-flex align-center justify-center"
            style="font-size: 35px"
          >
            {{ getTotalAmount() }}
          </v-card-subtitle>
          <v-card-actions>
            <v-btn outlined color="primary" to="/payrewards">Pay</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col class="text-center" cols="12" sm="3">
        <div class="cont">
          <v-card class="front-card" outlined>
            <v-card-text>
              <v-card class="d-flex flex-column rounded-xl">
                <div class="hackathon-img">
                  <img src="../assets/img/hac.png" alt="" />
                  <div class="icom">
                    <v-icon small class="subtitle-icon"
                      >mdi-star-outline</v-icon
                    >
                  </div>
                </div>

                <v-card-text class="start-hack">
                  <nuxt-link to="/companyform">
                    <v-list-item-subtitle
                      class="mb-2 pa-4 text-left line-height-ex"
                      style="font-size: 25px"
                    >
                      Start A <br />Hackathon
                    </v-list-item-subtitle>
                  </nuxt-link>
                </v-card-text>
              </v-card>
            </v-card-text>
          </v-card>
          <v-card class="back-card"></v-card>
        </div>
      </v-col>
    </v-row>
    <h2 class="text-left ma-4">Active Hackathons</h2>
    <v-row class="active-hackathons">
      <v-col
        class="text-centerc"
        cols="12"
        sm="6"
        v-for="hackathon in visibleHackathons"
        :key="hackathon.id"
      >
        <v-row>
          <v-col class="text-centerc" cols="12">
            <v-card>
              <v-list-item three-line>
                <v-list-item-content>
                  <v-col class="d-flex" style="gap: 30px">
                    <v-avatar class="user-avatar">
                      <v-icon>mdi-account</v-icon>
                    </v-avatar>
                    <v-list-item-title style="font-size: 20px">{{
                      hackathon.name
                    }}</v-list-item-title>
                  </v-col>
                  <v-col>
                    <v-list-item-title>{{
                      formatDate(hackathon.end_date)
                    }}</v-list-item-title>
                  </v-col>
                  <v-col>
                    <v-list-item-title>Active</v-list-item-title>
                  </v-col>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="text-centerc" cols="12" sm="12">
        <v-card class="theme--dark">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title
                class="mb-2 d-flex align-baseline"
                style="font-size: 25px"
                >Leader-Board</v-list-item-title
              >
              <v-progress-linear color="deep-orange"></v-progress-linear>
            </v-list-item-content>
          </v-list-item>
          <v-data-table
            :headers="headers"
            :items="leaderboard"
            @click:row="onRowClick"
          >
            <template v-slot:item.name="{ item }">
              <span>{{ item.user }}</span>
            </template>
            <template v-slot:item.status="{ item }">
              <span>{{ item.score }}</span>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
    <v-row> </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      headers: [
        { text: "Name", value: "name" },
        { text: "Score", value: "score" },
        // { text: "Type", value: "type" },
        // { text: "Date", value: "date" },
      ],

      users: [
        { username: "User1", profileImage: "user1.jpg", hasNewStory: true },
        { username: "User2", profileImage: "user2.jpg", hasNewStory: true },
        { username: "User3", profileImage: "user3.jpg", hasNewStory: true },
        { username: "User3", profileImage: "user3.jpg", hasNewStory: true },
        { username: "User3", profileImage: "user3.jpg", hasNewStory: true },
        // Add more user objects as needed
      ],
      maxVisible: 4,
      maxVisit: 2,
      showBorder: true,
      showPopup: false,
      showUserList: false,
      activeUsers: [],
      hackathons: [],
      leaderboard: [],
      rewards: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    onRowClick(item) {
      console.log(item);
    },
    formatDate(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleDateString();
    },
    getTotalAmount() {
      let total = 0;
      for (const reward of this.rewards) {
        total += reward.amt;
      }
      return total;
    },
    fetchData() {
      axios
        .get("http://127.0.0.1:8000/api/dashboard")
        .then((response) => {
          this.activeUsers = response.data.active_users;
          this.hackathons = response.data.hackathons;
          this.leaderboard = response.data.leaderboard;
          this.rewards = response.data.rewards;
          console.log("API Response:", response);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
  },

  computed: {
    displayedUsers() {
      const remainingCount = Math.max(0, this.users.length - this.maxVisible);
      const visibleUsers = this.users.slice(0, this.maxVisible);
      if (remainingCount > 0) {
        visibleUsers.push({
          isCount: true,
          count: remainingCount,
        });
      }
      return visibleUsers;
    },
    visibleHackathons() {
      return this.hackathons.slice(0, this.maxVisit);
    },
  },
};
</script>
<style scoped>
.start-hack:hover {
  cursor: pointer;
}
.v-application a {
  text-decoration: none;
  color: white;
}
img {
  width: 20%;
}
.hackathon-img {
  /* width: 10%; */
  display: flex;
  justify-content: space-between;
}
.line-height-ex {
  line-height: 1.5;
}
.cont {
  display: flex;
  justify-content: center;
  align-items: center;
}

.front-card {
  position: absolute;
  z-index: 2;
  top: 100px;
  border-radius: 2.25rem;
  width: 260px;
}

.back-card {
  height: 190px;
  width: 260px;
  border: dotted;
  position: relative;
  border-radius: 2.25rem;
  left: 23px;
}
.active-hackathons {
  overflow-x: auto !important;
}
.active-hackathons {
  white-space: nowrap;
}
.active-hackathons .v-col {
  display: inline-block;
  margin-right: 10px;
}
.v-card,
.v-data-table {
  background-color: #0f1724 !important;
}
.custom-border-dotted {
  border: 2px dotted;
}

.avatar-row {
  overflow: hidden;
  white-space: nowrap;
  margin-left: -40px;
}

.user-avatar {
  display: inline-block;
  width: 64px;
  height: 64px;
  margin-right: -32px;
  border: 2px solid transparent;
  background-size: cover;
  background-position: center;
  cursor: pointer;
  position: relative;
  z-index: 1;
}

.remaining-count-avatar {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 64px;
  height: 64px;
  margin-right: -32px;
  background-color: #f44336;
  position: relative;
  z-index: 1;
}

.remaining-count {
  font-size: 24px;
  color: white;
}
</style>
