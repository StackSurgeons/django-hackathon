<template>
  <v-container>
    <div class="publish-hackathon">
      <v-stepper
       
        color="transparent"
        style="background: transparent !important"
      >
        <v-stepper-items>
          <v-stepper-content step="1" class="pt-2">
            <form @submit.prevent="submitForm">
              <v-card>
                <v-card-title> Publish a Hackathon</v-card-title>
                <v-card-text>
                  <v-row>
                    <v-col cols="12">
                      <v-card-subtitle class="pa-0">
                        Name of Hackathon</v-card-subtitle
                      >
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        v-model="form.name"
                        label="Name"
                        outlined
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-card-subtitle class="pa-0">
                        Instruction</v-card-subtitle
                      >
                    </v-col>
                    <v-col cols="12">
                      <v-text-field
                        v-model="form.instruction"
                        placeholder="Extra Instruction"
                        outlined
                      />
                    </v-col>

                    <v-col cols="12" sm="4">
                      <v-text-field
                        v-model="form.startDate"
                        label="Start Date"
                        required
                        outlined
                        placeholder="yyyy/mm/dd "
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        v-model="form.endDate"
                        label="End Date"
                        required
                        outlined
                        placeholder="yyyy/mm/dd "
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12" sm="4">
                      <v-checkbox
                        v-model="form.private"
                        label="Private"
                      ></v-checkbox>
                    </v-col>

                    <v-col cols="12">
                      <v-card-subtitle class="pa-0">
                        Description</v-card-subtitle
                      >
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-textarea
                        v-model="form.description"
                        placeholder="Enter Contest Description"
                        auto-grow
                        outlined
                        rows="10"
                      ></v-textarea>
                    </v-col>
                    <v-col cols="12">
                      <v-card-subtitle class="pa-0 mt-5">
                        Problem Statement
                      </v-card-subtitle>
                    </v-col>
                    <v-col cols="12">
                      <v-textarea
                        v-model="form.problemStatement"
                        placeholder="Enter Problem Statement"
                        outlined
                      ></v-textarea>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field class="mt-8"
                        v-model="form.rewards"
                        label="Rewards"
                        required
                        outlined
                        placeholder="Enter Amount "
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="form.links"
                        label="External Links"
                        class="mt-8"
                        outlined
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" class="text-center">
                      <v-col cols="12">
                        <v-btn type="submit" color="primary">Submit</v-btn>
                      </v-col>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </form>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </div>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      // e1: 0,
      // closed: false,
      form: {
        name: "",
        description: "",
        private: false,
        startDate: "",
        endDate: "",
        rewards: "",
        problemStatement: "",
        links: "",
      },
    };
  },
  methods: {
    submitForm() {
      console.log(this.form);
    },
    resetForm() {
      this.form.name = "";
      this.form.description = "";
      this.form.private = false;
      this.form.startDate = "";
      this.form.endDate = "";
      this.form.links = "";
      this.form.rewards = "";
      this.form.problemStatement = "";
    },
  },
};
</script>

<style scoped>
.container {
  display: block !important;
  text-align: left !important;
}

.v-text-field {
  width: 100%;
}
.v-card__title {
  justify-content: left !important;
}

.form-container {
  display: flex;
  flex-direction: column;
}
label {
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[type="checkbox"] {
  margin-top: 5px;
}

button:hover {
  background-color: #0d47a1;
}
</style>
