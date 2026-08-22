import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';

const easeOut = [0.22, 1, 0.36, 1] as const;

interface FinalCTAProps {
  onEnterForge?: () => void;
}

export default function FinalCTA({ onEnterForge }: FinalCTAProps = {}) {
  return (
    <section
      id="enter"
      className="bg-grain relative overflow-hidden bg-background py-28 sm:py-36"
    >
      {/* faint dot-grid texture, centered */}
      <div
        className="bg-dot-grid pointer-events-none absolute inset-0 opacity-[0.35]"
        style={{
          maskImage:
            'radial-gradient(ellipse 50% 45% at 50% 50%, black 5%, transparent 70%)',
          WebkitMaskImage:
            'radial-gradient(ellipse 50% 45% at 50% 50%, black 5%, transparent 70%)',
        }}
      />

      <div className="relative mx-auto max-w-3xl px-6 text-center sm:px-8">
        {/* Small elegant illustration */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.8, ease: easeOut }}
          className="mx-auto mb-10 w-[100px] sm:mb-12 sm:w-[120px]"
        >
          <img
            src="/illustrations/cta-figure.png"
            alt="Hand-drawn illustration of a founder walking forward with purpose."
            className="w-full select-none opacity-80"
            draggable={false}
          />
        </motion.div>

        <motion.h2
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.8, ease: easeOut, delay: 0.08 }}
          className="font-display text-balance text-[2.5rem] leading-[1.06] tracking-[-0.01em] text-foreground sm:text-[3.2rem] lg:text-[3.8rem]"
        >
          Spend less time managing.
          <br />
          <span className="italic text-foreground-soft">
            More time building.
          </span>
        </motion.h2>

        <motion.p
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.7, ease: easeOut, delay: 0.22 }}
          className="mx-auto mt-6 max-w-md text-[1.05rem] leading-relaxed text-foreground-soft"
        >
          One workspace for the operational work behind your startup.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-80px' }}
          transition={{ duration: 0.7, ease: easeOut, delay: 0.34 }}
          className="mt-10"
        >
          <a
            href="#enter"
            onClick={(e) => {
              if (onEnterForge) {
                e.preventDefault();
                onEnterForge();
              }
            }}
            className="group inline-flex items-center gap-2.5 rounded-full bg-foreground px-7 py-4 text-[1rem] text-background transition-colors duration-300 hover:bg-accent"
          >
            Enter FORGE
            <ArrowRight className="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1" />
          </a>
        </motion.div>
      </div>
    </section>
  );
}
