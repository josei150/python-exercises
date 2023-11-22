class Allergies:

    allergies: list[tuple[str, int]] = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score: int):
        if score > 255:
            self.score = score - 256
        else:
            self.score = score
        self.allergies_user: list[str] = []
        reverse_allergies = sorted(
            self.allergies, key=lambda allergy: allergy[1], reverse=True)
        score = 0
        for allergy in reverse_allergies:
            if allergy[1] + score > self.score:
                continue
            if score >= self.score:
                break
            self.allergies_user.append(allergy[0])
            score += allergy[1]

    def allergic_to(self, item: str) -> bool:
        return item in self.allergies_user

    @property
    def lst(self) -> list[str]:
        self.allergies_user = list(reversed(self.allergies_user))
        return self.allergies_user


if __name__ == "__main__":
    allergy = Allergies(1).lst
    print(allergy)
    # print(allergy.allergic_to("pollen"))
    # print(allergy.lst)
