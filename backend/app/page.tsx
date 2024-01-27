import { FeatureSection } from "@/components/Landing/FeatureSection";
import { HeroSection } from "@/components/Landing/HeroSection";
import { LandingContainer } from "@/components/Landing/LandingContainer";

export default function Home() {
  return (
    <LandingContainer>
      <HeroSection />
      <FeatureSection title="Features" />
    </LandingContainer>
  );
}
