<template>
  <v-container>
    <v-row>
      <!-- Rank Leaderboard Section -->
      <v-col cols="12" sm="5">
        <v-card>
          <v-card-text class="justify-center">
            <v-list>
              <v-list-item v-for="(user, index) in sortedUsers" :key="user.id">
                <v-list-item-content>
                  <v-list-item-title>{{ user.name }}</v-list-item-title>
                  <v-list-item-subtitle>
                    Registered: {{ formatDate(user.registrationDate) }}
                  </v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <v-badge :content="index + 1" color="primary">
                    <template v-slot:badge>
                      <v-icon small>mdi-crown</v-icon>
                    </template>
                  </v-badge>
                </v-list-item-action>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Rewards Section -->
      <v-col cols="12" sm="4">
        <v-card>
          <v-card-text class="justify-center reward-card align-center">
            <v-list>
              <v-list-item>
                <v-list-item-subtitle class="mb-2" style="font-size: 25px">
                  Rewards
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-card-subtitle
                  class="d-flex align-center justify-center"
                  style="font-size: 35px"
                >
                  ${{ rewardAmount }}
                </v-card-subtitle>
              </v-list-item>
              <v-list-item>
                <v-btn outlined color="primary" @click="claimReward">
                  Claim Reward
                </v-btn>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col col="12" sm="3">
        <v-card class="private_contest-card">
          <v-card-title>Private Contest</v-card-title>
          <v-card-text>
            <v-text-field
              v-model="contestLink"
              label="Contest Link"
              outlined
            ></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="joinContest">Join</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="isClaimPopupVisible" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">Claim Reward</v-card-title>
        <v-card-text class="justify-center">
          <v-form @submit.prevent="submitClaim">
            <v-text-field
              v-model="upiId"
              label="UPI ID"
              required
              outlined
            ></v-text-field>
            <v-btn type="submit" color="primary" class="mt-2">Submit</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
    <!-- Active Hackathons Section -->
    <h2 class="text-left mt-5">Active Hackathons</h2>
    <v-col
      v-for="(hackathon, index) in activeHackathons"
      :key="index"
      cols="12"
      class="hacks-card"
    >
      <v-card class="hackathon-card">
        <v-card-text>
          <v-row align="center" justify="space-between">
            <v-col cols="auto">
              <h3>{{ hackathon.name }}</h3>
            </v-col>
            <v-col cols="auto">
              <p class="hackathon-date">End Date: {{ hackathon.endDate }}</p>
            </v-col>
            <v-col cols="auto">
              <v-btn
                outlined
                color="primary"
                @click="joinChallenge(hackathon.id)"
              >
                Join Challenge
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
    <!-- Past Hackathons Section -->
    <h2 class="mt-5 text-left">Past Hackathons</h2>
    <v-col
      v-for="(hackathon, index) in pastHackathons"
      :key="index"
      cols="12"
      class="hacks-card"
    >
      <v-card class="hackathon-card">
        <v-card-text>
          <v-row align="center" justify="space-between">
            <v-col cols="auto">
              <h3>{{ hackathon.name }}</h3>
            </v-col>
            <v-col cols="auto">
              <p class="hackathon-date">End Date: {{ hackathon.endDate }}</p>
            </v-col>
            <v-col cols="auto">
              <v-btn outlined color="primary" disabled> View Results </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      users: [
        { id: 1, name: "User 1", registrationDate: new Date("2023-06-25") },
        { id: 2, name: "User 2", registrationDate: new Date("2023-06-26") },
        { id: 3, name: "User 3", registrationDate: new Date("2023-06-24") },
      ],
      activeHackathons: [
        { id: 1, name: "Hackathon 1", endDate: "2023-07-15" },
        { id: 2, name: "Hackathon 2", endDate: "2023-08-20" },
        { id: 3, name: "Hackathon 3", endDate: "2023-09-10" },
      ],
      pastHackathons: [
        { id: 1, name: "Past Hackathon 1", endDate: "2023-06-15" },
        { id: 2, name: "Past Hackathon 2", endDate: "2023-07-20" },
        { id: 3, name: "Past Hackathon 3", endDate: "2023-08-10" },
      ],
      rewardAmount: 0,
      isClaimPopupVisible: false,
      upiId: "",
    };
  },
  computed: {
    sortedUsers() {
      return this.users.sort((a, b) => a.registrationDate - b.registrationDate);
    },
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    joinChallenge(hackathonId) {
      this.$router.push("/overview");
    },
    claimReward() {
      this.isClaimPopupVisible = true;
    },
    submitClaim() {
      this.isClaimPopupVisible = false;
      this.upiId = ""; // Clearing the UPI ID field
    },
  },
};
</script>

<style scoped>
.hacks-card {
  padding: 0 !important;
  margin-bottom: 5px;
}
.reward-card,
.private_contest-card {
  height: 235px;
}
.private_contest-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
